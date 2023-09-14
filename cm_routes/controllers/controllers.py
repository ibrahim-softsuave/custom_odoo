# -*- coding: utf-8 -*-
# from odoo import http


# class CmRoutes(http.Controller):
#     @http.route('/cm_routes/cm_routes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cm_routes/cm_routes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cm_routes.listing', {
#             'root': '/cm_routes/cm_routes',
#             'objects': http.request.env['cm_routes.cm_routes'].search([]),
#         })

#     @http.route('/cm_routes/cm_routes/objects/<model("cm_routes.cm_routes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cm_routes.object', {
#             'object': obj
#         })
