from odoo import http
from odoo.http import request
class WebFormController(http.Controller):


    @http.route('/register', type='http', auth='public', website=True)
    def web_form(self, **kwargs):
        registers = request.env['school.registration'].sudo().search([])
        if kwargs.get('default_id'):
            print('id',default_id)
        return request.render('school_management.web_register_list_template',{'registers':registers})

    @http.route('/register/edit', type='http', auth='public', website=True)
    def action_edit(self, **kwargs):
        print('id',kwargs.get('edit'))


    @http.route('/register/register-new', auth='public', website=True)
    def display_web_form(self, **kwargs):
       return request.render('school_management.web_form_template')


    @http.route('/webform/submit', type='http', auth='public', website=True, methods=['POST'])
    def handle_web_form_submission(self, **post):
       request.env['school.registration'].sudo().create({
           'firstname': post.get('firstname'),
           'lastname': post.get('lastname',''),
           'email': post.get('email'),
           'father': post.get('father',''),
           'mother': post.get('mother',''),
           'phone': post.get('phone',''),
           'gender': post.get('gender',''),
           'dob': post.get('dob',''),
           'communication_address': post.get('address',''),
       })
       return request.redirect('/thank-you-page')

    @http.route('/leaves', type='http', auth='public', website=True)
    def leave_web_form(self, **kwargs):
       students = request.env['school.students'].sudo().search([])
       return request.render('school_management.web_leaves_template',{'students':students})

    @http.route('/leaves/submit', type='http', auth='public', website=True, methods=['POST'])
    def leave_web_form_submission(self, **post):
       print('student',post.get('studentss'))
       request.env['school.leaves'].sudo().create({
           'students_id': post.get('studentss'),
           'start_date': post.get('start_date'),
           'end_date': post.get('end_date'),
           'half_day': post.get('half_day'),
           'reason': post.get('reason',''),
       })
       return request.redirect('/thank-you-page')

    @http.route('/events', type='http', auth='public', website=True)
    def web_events_form(self, **kwargs):
       clubs = request.env['school.clubs'].sudo().search([])
       partners = request.env['res.partner'].sudo().search([])
       return request.render('school_management.web_events_template',
                             {'clubs':clubs,'partners':partners})
    @http.route('/events/submit', type='http', auth='public', website=True, methods=['POST'])
    def web_event_submission(self, **post):
       request.env['school.events'].sudo().create({
           'name': post.get('name'),
           'clubs_id': post.get('clubs'),
           'date_begin': post.get('date_begin'),
           'date_end': post.get('date_end'),
           'organizer_id': post.get('organizer'),
           'description': post.get('description',''),
           'active': post.get('active'),
       })
       return request.redirect('/thank-you-page')

    @http.route('/thank-you-page', type='http', auth='public', website=True)
    def thank_you_page(self, **kwargs):
       return request.render('school_management.web_thankyou_template')
