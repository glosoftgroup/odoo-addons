# -*- coding: utf-8 -*-
from odoo import http

# class ExtendProductTemplate(http.Controller):
#     @http.route('/extend_product_template/extend_product_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extend_product_template/extend_product_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extend_product_template.listing', {
#             'root': '/extend_product_template/extend_product_template',
#             'objects': http.request.env['extend_product_template.extend_product_template'].search([]),
#         })

#     @http.route('/extend_product_template/extend_product_template/objects/<model("extend_product_template.extend_product_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extend_product_template.object', {
#             'object': obj
#         })