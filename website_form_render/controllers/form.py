from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/my/custom/form', auth='public', website=True)
    def custom_page(self, **kwargs):
        return request.render('website_form_render.custom_form_render')

    @http.route('/my/custom/page/submit', type='http', auth='public', website=True, csrf=False)
    def custom_page_submit(self, **post):
        errors = []
        if not post.get('name'):
            errors.append('Name is required.')
        if not post.get('mobile'):
            errors.append('Mobile number is required.')
        if not post.get('email'):
            errors.append('Email is required.')
        if not post.get('address'):
            errors.append('Address is required.')

        if errors:
            return request.render('website_form_render.custom_form_render', {'error': True, 'errors': errors})

        return request.render('website_form_render.custom_form_render', {'success': True})

