from odoo import api, fields, models, tools, _


class Company(models.Model):
    _inherit = "res.company"
    
    @api.model
    def _lang_get(self):
        return self.env['res.lang'].get_installed()
    
    lang = fields.Selection(_lang_get, string='Language', default=lambda self: self.env.lang,
                            help="All the emails and documents sent to this contact will be translated in this language.")