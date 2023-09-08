# -*- coding: utf-8 -*-
# from odoo import http


# class CmInhiritence(http.Controller):
#     @http.route('/cm_inhiritence/cm_inhiritence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cm_inhiritence/cm_inhiritence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cm_inhiritence.listing', {
#             'root': '/cm_inhiritence/cm_inhiritence',
#             'objects': http.request.env['cm_inhiritence.cm_inhiritence'].search([]),
#         })

#     @http.route('/cm_inhiritence/cm_inhiritence/objects/<model("cm_inhiritence.cm_inhiritence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cm_inhiritence.object', {
#             'object': obj
#         })
