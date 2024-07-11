from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_view(self, view_id=None, view_type='form', **options):
        arch, view = super(ResPartner, self)._get_view(view_id, view_type, **options)
        is_manager = self.env.user.has_group('sales_team.group_sale_manager')
        if view_type == 'form' and not is_manager:
            for node in arch.xpath("//field"):
                node.set('readonly', '1')
        return arch, view
