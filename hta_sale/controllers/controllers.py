# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSale(http.Controller):
#     @http.route('/hta_sale/hta_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_sale/hta_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_sale.listing', {
#             'root': '/hta_sale/hta_sale',
#             'objects': http.request.env['hta_sale.hta_sale'].search([]),
#         })

#     @http.route('/hta_sale/hta_sale/objects/<model("hta_sale.hta_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_sale.object', {
#             'object': obj
#         })
