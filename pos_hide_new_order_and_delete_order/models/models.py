# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pos_custom_receipt_dunia_bangunan(models.Model):
#     _name = 'pos_custom_receipt_dunia_bangunan.pos_custom_receipt_dunia_bangunan'
#     _description = 'pos_custom_receipt_dunia_bangunan.pos_custom_receipt_dunia_bangunan'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
