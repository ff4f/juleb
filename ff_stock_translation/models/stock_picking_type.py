from odoo import api, fields, models, SUPERUSER_ID, _

class PickingType(models.Model):
    _inherit = "stock.picking.type"
    
    @api.model
    def create(self, vals):
        company_id = self.env['res.company'].browse([(vals.get('company_id'))])
        if self.env['ir.config_parameter'].sudo().get_param('ff_stock_translation.is_multi_language'):
            translation = self.env['ir.translation'].sudo().search([('src','=',vals.get('name')),('lang','=',company_id.lang)],limit=1)
            if translation:
                vals['name'] = translation.value

        return super(PickingType, self).create(vals)
