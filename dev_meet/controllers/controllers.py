# -*- coding: utf-8 -*-
# from odoo import http


# class DevMeet(http.Controller):
#     @http.route('/dev_meet/dev_meet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_meet/dev_meet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_meet.listing', {
#             'root': '/dev_meet/dev_meet',
#             'objects': http.request.env['dev_meet.dev_meet'].search([]),
#         })

#     @http.route('/dev_meet/dev_meet/objects/<model("dev_meet.dev_meet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_meet.object', {
#             'object': obj
#         })
