# -*- coding: utf-8 -*-
from odoo import http

# class ExtendDashboardTemplate(http.Controller):
#     @http.route('/extend_dashboard_template/extend_dashboard_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extend_dashboard_template/extend_dashboard_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extend_dashboard_template.listing', {
#             'root': '/extend_dashboard_template/extend_dashboard_template',
#             'objects': http.request.env['extend_dashboard_template.extend_dashboard_template'].search([]),
#         })

#     @http.route('/extend_dashboard_template/extend_dashboard_template/objects/<model("extend_dashboard_template.extend_dashboard_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extend_dashboard_template.object', {
#             'object': obj
#         })