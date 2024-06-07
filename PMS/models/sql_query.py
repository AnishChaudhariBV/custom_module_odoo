from odoo import models, fields, api, _

class CheckQuery(models.Model):
    _name = 'sale.reports'
    _description = 'Sql Query'

    property_type = fields.Selection([
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('industrial', 'Industrial')],
        string='Property Type'
    )
    name = fields.Char(string='Property Name/Title')
    address = fields.Char(string='Address')
    description = fields.Char(string='Description')
    price = fields.Float(string='Price/Rent')
    property_size = fields.Float(string='Property Size/Area')
    bedrooms = fields.Integer(string='Number of Bedrooms')
    bathrooms = fields.Integer(string='Number of Bathrooms')
    availability_status = fields.Selection([
        ('available', 'Available'),
        ('under_contract', 'Under Contract'),
        ('rented', 'Rented')],
        string='Availability Status'
    )
    contact_name = fields.Char(string='Contact Name', required=True)
    contact_phone = fields.Char(string='Contact Phone', required=True)
    contact_email = fields.Char(string='Contact Email')
    additional_details = fields.Text(string='Additional Details')
    date_listed = fields.Date(string='Date Listed', default=fields.Date.today)
    property_id = fields.Char(string='Property ID/Reference Number', required=True)

    listed_property_count = fields.Integer(string='Listed Property Count')

    def _select(self):
        return """
            property_type,
            name,
            address,
            description,
            price,
            property_size,
            bedrooms,
            bathrooms,
            availability_status,
            contact_name,
            contact_phone,
            contact_email,
            additional_details,
            date_listed,
            property_id,
            COUNT(*) OVER() AS listed_property_count
        """

    def _from(self):
        return "property_list"

    def _where(self):
        where_conditions = ["price > 5000"]  # Filter records with price greater than 5000

        if self.property_type:
            where_conditions.append(f"property_type = '{self.property_type}'")
        if self.availability_status:
            where_conditions.append(f"availability_status = '{self.availability_status}'")

        where_clause = " AND ".join(where_conditions)
        return where_clause

    def _group_by(self):
        return ""

    def _order_by(self):
        return "date_listed DESC"

    def _query(self):
        select_clause = self._select()
        from_clause = self._from()
        where_clause = self._where() or ""
        group_by_clause = self._group_by() or ""
        order_by_clause = self._order_by() or ""

        return f"""
            SELECT {select_clause}
            FROM {from_clause}
            {"WHERE " + where_clause if where_clause else ""}
            {"GROUP BY " + group_by_clause if group_by_clause else ""}
            {"ORDER BY " + order_by_clause if order_by_clause else ""}
        """

    @property
    def _table_query(self):
        return self._query()
