# -*- coding: utf-8 -*-
{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'School management for school',
    'description': """
     School management
     =================
     Used for managing the records of students in school
     """,
    'category': 'SchoolManagement/SchoolManagement',
    'depends': [
        'base', 'mail', 'sale_management', 'contacts', 'web', 'website'],
    'data': [
        'data/ir_sequence_data.xml',
        'data/school_department_data.xml',
        'data/school_class_data.xml',
        'data/school_subject_data.xml',
        'data/base_automation_data.xml',
        'data/email_template_data.xml',
        'data/ir_cron_data.xml',
        'security/school_management_groups.xml',
        'security/school_management_rule_company.xml',
        'security/ir.model.access.csv',
        'views/school_department_views.xml',
        'views/school_registration_views.xml',
        'wizard/school_registration_wizard_view.xml',
        'views/school_students_views.xml',
        'views/school_class_views.xml',
        'views/school_subject_views.xml',
        'views/school_academic_year_views.xml',
        'views/school_events_views.xml',
        'views/school_clubs_views.xml',
        'views/sale_order_views.xml',
        'views/res_partner_views.xml',
        'views/school_leaves_views.xml',
        'wizard/school_student_report_wizard_views.xml',
        'wizard/school_club_report_wizard_views.xml',
        'wizard/school_leave_report_wizard_views.xml',
        'report/leave_report_template.xml',
        'report/student_template_report.xml',
        'report/club_template_report.xml',
        'report/school_report_action.xml',
        'views/school_exams_views.xml',
        'views/school_management_menus.xml',
        'views/website_form_template.xml',
        'views/website_register_menu.xml'
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'school_management/static/src/js/action_manager.js'
        ]
    }
}
