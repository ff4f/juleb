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
    
    
    def change_translation_name(self, lang):
        if self.company_id.lang is not 'en_US' and lang != 'en_US':
            translation = self.env['ir.translation'].sudo().search([('value','=',self.name),('lang','=',self.company_id.lang)],limit=1)
            if translation:
                value = self.env['ir.translation'].sudo().search([('src','=',translation.src),('lang','=',lang)],limit=1).value
                self.name = value
        else:
            # translation = self.env['ir.translation'].sudo().search([('src','=',self.name),('lang','=',lang)],limit=1)
            translation = self.env['ir.translation'].sudo().search([('value','=',self.name),('lang','=',self.company_id.lang)],limit=1)
            if translation:
                self.name = translation.src
        return True