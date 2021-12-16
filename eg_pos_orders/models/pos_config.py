from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    order_list_selection = fields.Selection(
        [('today_order', 'Load All Today Orders'), ('current_session', 'Load Orders of Current Session'),
         ('past_orders', 'Load All Past Orders'),
         ('days', 'Load Orders of Last "n" Days')], default='today_order', string='Load POS Order')
    selected_days = fields.Integer(string='Days')
