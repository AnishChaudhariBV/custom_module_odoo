from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError


class MyController(http.Controller):

    @http.route('/my/custom/form', auth='public', website=True)
    def custom_page(self, **kwargs):
        return request.render('website_form_render.custom_form_render')

    @http.route('/my/custom/page/submit', type='http', auth='public', website=True, csrf=False)
    def custom_page_submit(self, **post):
        required_fields = {
            'name': 'Name is required.',
            'mobile': 'Mobile number is required.',
            'email': 'Email is required.',
            'address': 'Address is required.',
        }

        errors = [error for field, error in required_fields.items() if not post.get(field)]

        if errors:
            return request.render('website_form_render.custom_form_render', {'error': True, 'errors': errors})

        form_data = {
            'name': post.get('name'),
            'mobile': post.get('mobile'),
            'email': post.get('email'),
            'address': post.get('address'),
        }

        try:
            if request.env.user.has_group('base.group_public'):
                custom_form_data = request.env['custom.form.data'].create(form_data)
            else:
                signin_user_data = request.env['signin.user.data'].create(form_data)
        except ValidationError as e:
            # Capture the general error message
            errors['general'] = str(e)
            return request.render('website_form_render.custom_form_render', {'error': True, 'errors': errors})

        return request.render('website_form_render.custom_form_render', {'success': True})
