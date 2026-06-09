# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from datetime import datetime
import uuid
class WebsiteEvent(http.Controller):
   @http.route('/get_latest_event', auth="public", type='jsonrpc',
               website=True)
   def get_latest_event(self):
       """Get the website categories for the snippet."""
       events = request.env[
           'school.events'].sudo().search([],limit=10)
       values = {}

       for event in events:
           event_list = []
           uniId=uuid.uuid4()
           if event.poster:
               decode = event.poster.decode('utf-8')
           else:
               decode = False
           time = datetime.now().microsecond
           print('time',time)
           event_list.append(event.name)
           event_list.append(decode)
           event_list.append(event.description)
           event_list.append(time)
           values[event.id] = event_list
           values['unique_id'] = uniId
           print(event_list[2])
       return values


   @http.route('/events/view/<int:record_id>', type='http', auth='public', website=True)
   def events_view(self,record_id, **post):
       print('record',record_id)
       event = request.env['school.events'].sudo().browse(record_id)
       print('event_club',event.active)
       if event.poster:
           poster = event.poster.decode('utf-8')
       else:
           poster = False
       return request.render('school_management.web_event_view_template',{'event':event,'poster':poster})



