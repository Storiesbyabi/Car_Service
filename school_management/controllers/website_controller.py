from odoo import http
from odoo.http import request
class WebFormController(http.Controller):
   @http.route('/register', auth='public', website=True)
   def display_web_form(self, **kwargs):
       return request.render('school_management.web_form_template')
   # @http.route('/webform/submit', type='http', auth='public', website=True, methods=['POST'])
   # def handle_web_form_submission(self, **post):
   #     request.env['custom.web.form.booking'].sudo().create({
   #         'name': post.get('name'),
   #         'phone': post.get('phone'),
   #         'email': post.get('email'),
   #     })
   #     return request.redirect('/thank-you-page')
