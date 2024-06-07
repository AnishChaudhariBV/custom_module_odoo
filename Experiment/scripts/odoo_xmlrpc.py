from xmlrpc import client as xmlrpclib
import base64

# Odoo server details
url = "http://localhost:8069"
db = "test__17"
username = "admin"
password = "admin"

# Connect to the common endpoint
common = xmlrpclib.ServerProxy(f"{url}/xmlrpc/2/common")
a=common.version()
print(a)
# Authenticate
uid = common.authenticate(db, username, password, {})
if uid:
    print(f"Authenticated as user with ID: {uid}")
else:
    print("Failed to authenticate")

# model='res.partner'
# model='property.inquiry'
# search=[]
# search=[['is_company', '=', True]]
# method='search'

# operations=xmlrpclib.ServerProxy(f"{url}/xmlrpc/2/object")
# list_of_ids=operations.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
# print(list_of_ids)
# list_of_ids=operations.execute(db,uid,password,model,method,search)
# print(list_of_ids)

#
# method='read'
# list_of_ids=operations.execute(db,uid,password,model,method,list_of_ids)
# for customer in list_of_ids:
#     print(customer['id'],customer['name'],customer['phone'],customer['email'])


# method='fields_get'
# fields_details=operations.execute(db,uid,password,model,method,[])
# print(len(fields_details))
#
# model='property.inquiry'
# method='create'
# list_of_create=operations.execute(db,uid,password,model,method,{'name':'veer','phone':"4567678855899"})
# print(list_of_create)
# model='res.partner'
# print(list_of_write)
#
#
models = xmlrpclib.ServerProxy(f"{url}/xmlrpc/2/object")
# Define the model and method
# model = 'property.list'
# search_method = 'search'
# write_method = 'write'
#
# # Search for records
# list_of_search = models.execute(db, uid, password, model, search_method, [])
# print(list_of_search)
#
# # Update each record
# for record_id in list_of_search:
#     list_of_write = models.execute(db, uid, password, model, write_method, [record_id], {'contact_name': 'Anish'})
#     print(list_of_write)
#
#


# Example: Search for sale orders
# sale_orders = models.execute_kw(db, uid, password, 'sale.order', 'search_read',
#                                 [[['state', '=', 'draft']]], {'fields': ['name', 'amount_total']})

# Search for sale orders
# sale_order_ids = models.execute_kw(db, uid, password, 'sale.order', 'search', [[]])
#
# # Iterate over each sale order and send the quotation
# for sale_order_id in sale_order_ids:
#     mail_sent = models.execute_kw(db, uid, password, 'sale.order',
#                                   'action_quotation_send', [[sale_order_id]])
#     print("Quotation sent for sale order with ID:", sale_order_id)

# sale_orders = models.execute_kw(db, uid, password, 'sale.order', 'search_read', [[]], {'limit': 1})

# Fetch draft invoices
# draft_invoices = models.execute_kw(db, uid, password, 'account.move', 'search',
#                                    [[['state', '=', 'draft']]])
# print(draft_invoices)

# Read the partner_id field for each draft invoice
# invoice_details = models.execute_kw(db, uid, password, 'account.move', 'read', [draft_invoices, ['partner_id']])

# Confirm all draft invoices with a customer
# for invoice in invoice_details:
#     invoice_id = invoice['id']
#     partner_id = invoice['partner_id']
#     if partner_id:
#         print(f"Confirming invoice ID: {invoice_id}")
#         models.execute_kw(db, uid, password, 'account.move', 'action_post', [[invoice_id]])
#         print(f"Invoice ID: {invoice_id} confirmed.")
#     else:
#         print(f"Skipping invoice ID: {invoice_id} as it has no customer assigned.")

# #
#
# print("All draft invoices confirmed.")
#
#
# draft_invoices = models.execute_kw(
#         db, uid, password,
#         'account.move', 'search_read',
#         [[['state', '=', 'posted']]]
#     )
#
# print(draft_invoices)
# print(len(draft_invoices))


# a=models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
# print(a)
