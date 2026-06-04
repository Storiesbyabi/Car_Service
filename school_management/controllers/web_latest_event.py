# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
class WebsiteEvent(http.Controller):
   @http.route('/get_latest_event', auth="public", type='jsonrpc',
               website=True)
   def get_latest_event(self):
       """Get the website categories for the snippet."""
       events = request.env[
           'school.events'].sudo().search([],limit=2)
       values = {}
       for event in events:
           values[event.id] = event.name

       print(values)
       return values

   # @http.route('/events/view/<int:record_id>', type='http', auth='public', website=True, methods=['POST'])
   # def events_view(self,record_id, **post):
   #     event = request.env['school.events'].sudo().browse(int(record_id))
   #     print('event',event)
