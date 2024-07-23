from odoo import http
from odoo.http import request

class CustomFormController(http.Controller):

    @http.route('/custom/form', type='http', auth='public', website=True)
    def custom_form(self, **kwargs):
        records = request.env['custom.form'].sudo().search([])
        return request.render('edit_at_portal_level_task.custom_form_template', {
            'records': records,
        })

    @http.route('/custom/form/new', type='http', auth='public', website=True)
    def custom_form_new(self, **kwargs):
        return request.render('edit_at_portal_level_task.custom_form_show_template', {})

    @http.route('/custom/form/submit', type='http', auth='public', website=True, csrf=False)
    def custom_form_submit(self, **kwargs):
        if kwargs:
            request.env['custom.form'].sudo().create({
                'name': kwargs.get('name'),
                'email': kwargs.get('email'),
                'phone': kwargs.get('phone'),
                'message': kwargs.get('message'),
            })
        return request.redirect('/custom/form')

    @http.route('/custom/form/edit/<int:record_id>', type='http', auth='public', website=True)
    def custom_form_edit(self, record_id, **kwargs):
        record = request.env['custom.form'].sudo().browse(record_id)
        if record.exists():
            return request.render('edit_at_portal_level_task.custom_form_edit_template', {
                'record': record,
            })
        return request.redirect('/custom/form')

    @http.route('/custom/form/update/<int:record_id>', type='http', auth='public', website=True, csrf=False)
    def custom_form_update(self, record_id, **kwargs):
        record = request.env['custom.form'].sudo().browse(record_id)
        if record.exists() and kwargs:
            record.sudo().write({
                'name': kwargs.get('name'),
                'email': kwargs.get('email'),
                'phone': kwargs.get('phone'),
                'message': kwargs.get('message'),
            })
        return request.redirect('/custom/form')

    @http.route('/custom/form/delete/<int:record_id>', type='http', auth='public', website=True, csrf=False)
    def custom_form_delete(self, record_id, **kwargs):
        record = request.env['custom.form'].sudo().browse(record_id)
        if record.exists():
            record.sudo().unlink()
        return request.redirect('/custom/form')
