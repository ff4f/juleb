from odoo import api, fields, models, SUPERUSER_ID


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_multi_language = fields.Boolean(string='Multi Language', default=False,
                                    config_parameter='ff_stock_translation.is_multi_language')
    
    