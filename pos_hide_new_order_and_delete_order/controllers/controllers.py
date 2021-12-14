# -*- coding: utf-8 -*-
# from odoo import http


# class PosCustomReceipt(http.Controller):
#     @http.route('/pos_custom_receipt_dunia_bangunan/pos_custom_receipt_dunia_bangunan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_custom_receipt_dunia_bangunan/pos_custom_receipt_dunia_bangunan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_custom_receipt_dunia_bangunan.listing', {
#             'root': '/pos_custom_receipt_dunia_bangunan/pos_custom_receipt_dunia_bangunan',
#             'objects': http.request.env['pos_custom_receipt_dunia_bangunan.pos_custom_receipt_dunia_bangunan'].search([]),
#         })

#     @http.route('/pos_custom_receipt_dunia_bangunan/pos_custom_receipt_dunia_bangunan/objects/<model("pos_custom_receipt_dunia_bangunan.pos_custom_receipt_dunia_bangunan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_custom_receipt_dunia_bangunan.object', {
#             'object': obj
#         })
