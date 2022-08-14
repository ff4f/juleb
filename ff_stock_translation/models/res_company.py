from odoo import api, fields, models, tools, _


class Company(models.Model):
    _inherit = "res.company"
    
    @api.model
    def _lang_get(self):
        return self.env['res.lang'].get_installed()
    
    lang = fields.Selection(_lang_get, string='Language', default=lambda self: self.env.lang,
                            help="All the emails and documents sent to this contact will be translated in this language.")

    def write(self, values):
        if values.get('lang') and self.env['ir.config_parameter'].sudo().get_param('ff_stock_translation.is_multi_language'):
            picking_type = self.env['stock.picking.type'].search([('company_id','=',self.id)])
            for picking in picking_type:
                picking.change_translation_name(values.get('lang'))
        return super(Company, self).write(values)
