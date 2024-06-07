import xlsxwriter
from io import BytesIO
import base64
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ExcelReport(models.TransientModel):
    _name = 'excel.report'
    _description = 'Excel Report'

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError("Start Date should be before or equal to End Date.")

    def print_report(self):
        # Generate Excel report
        file_data = BytesIO()
        workbook = xlsxwriter.Workbook(file_data)

        # Create the first sheet for sales orders
        worksheet_orders = workbook.add_worksheet('Sales Orders')

        # Define formats
        title_format = workbook.add_format({
            'bold': True, 'font_size': 16, 'align': 'center', 'valign': 'vcenter',
            'bg_color': '#4F81BD', 'font_color': 'white'
        })
        header_format = workbook.add_format({
            'bold': True, 'bg_color': '#D7E4BC', 'border': 1,
            'align': 'center', 'valign': 'vcenter'
        })
        cell_format = workbook.add_format({
            'border': 1, 'valign': 'vcenter'
        })
        date_format = workbook.add_format({
            'border': 1, 'num_format': 'yyyy-mm-dd', 'valign': 'vcenter'
        })
        amount_format = workbook.add_format({
            'border': 1, 'num_format': '#,##0.00', 'valign': 'vcenter','align':'right'
        })

        # Set column widths for orders sheet
        worksheet_orders.set_column('A:A', 20)  # Order Reference
        worksheet_orders.set_column('B:B', 30)  # Customer
        worksheet_orders.set_column('C:C', 15)  # Order Date
        worksheet_orders.set_column('D:D', 15)  # Total Amount

        # Add a title for orders sheet
        title = f'Sales Report {self.start_date} to {self.end_date}'
        worksheet_orders.merge_range('A1:D1', title, title_format)

        # Add a header for orders sheet
        headers = ['Order Reference', 'Customer', 'Order Date', 'Total Amount']
        for col_num, header in enumerate(headers):
            worksheet_orders.write(1, col_num, header, header_format)

        # Fetch orders within the date range
        orders = self.env['sale.order'].search([
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date)
        ])

        # Write order data to the orders sheet
        for row_num, order in enumerate(orders, start=2):
            worksheet_orders.write(row_num, 0, order.name, cell_format)
            worksheet_orders.write(row_num, 1, order.partner_id.name, cell_format)
            worksheet_orders.write(row_num, 2, str(order.date_order), date_format)
            worksheet_orders.write(row_num, 3, f"{order.amount_total} {order.currency_id.symbol}", amount_format)

        # Create the second sheet for product data
        worksheet_products = workbook.add_worksheet('Products')

        # Set column widths for products sheet
        worksheet_products.set_column('A:A', 30)  # Product Name
        worksheet_products.set_column('B:B', 20)  # Quantity Ordered
        worksheet_products.set_column('C:C', 20)  # Total Sales
        worksheet_products.set_column('D:D', 20)  # On-Hand Quantity

        # Add a header for products sheet
        product_headers = ['Product Name', 'Quantity Ordered', 'Total Sales', 'On-Hand Quantity']
        for col_num, header in enumerate(product_headers):
            worksheet_products.write(0, col_num, header, header_format)

        # Fetch order lines within the date range
        order_lines = self.env['sale.order.line'].search([
            ('order_id.date_order', '>=', self.start_date),
            ('order_id.date_order', '<=', self.end_date)
        ])

        # Aggregate product data
        product_data = {}
        for line in order_lines:
            product = line.product_id
            if product in product_data:
                product_data[product]['quantity'] += line.product_uom_qty
                product_data[product]['total_sales'] += line.price_subtotal
            else:
                product_data[product] = {
                    'quantity': line.product_uom_qty,
                    'total_sales': line.price_subtotal,
                    'currency': line.order_id.currency_id.symbol,
                    'on_hand_qty': product.qty_available  # Fetching on-hand quantity
                }

        # Write product data to the products sheet
        for row_num, (product, data) in enumerate(product_data.items(), start=1):
            worksheet_products.write(row_num, 0, product.name, cell_format)
            worksheet_products.write(row_num, 1, data['quantity'], cell_format)
            worksheet_products.write(row_num, 2, f"{data['total_sales']} {data['currency']}", amount_format)
            worksheet_products.write(row_num, 3, data['on_hand_qty'], cell_format)

        # Close the workbook and get the data
        workbook.close()
        file_data.seek(0)
        report_data = file_data.read()

        # Base64 encode the report data
        encoded_report_data = base64.b64encode(report_data).decode('utf-8')

        # Create the attachment
        attachment = self.env['ir.attachment'].create({
            'name': 'Sales Report.xlsx',
            'type': 'binary',
            'datas': encoded_report_data,
            'store_fname': 'sales_report.xlsx',
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }
