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
        'base', 'mail', 'sale_management', 'contacts', 'purchase'],
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
        'views/product_template_views.xml',
        'wizad/school_registration_wizard_view.xml',
        'wizad/rfq_wizard_views.xml',
        'views/school_students_views.xml',
        'views/school_class_views.xml',
        'views/school_subject_views.xml',
        'views/school_academic_year_views.xml',
        'views/school_events_views.xml',
        'views/school_clubs_views.xml',
        'views/sale_order_views.xml',
        'views/res_partner_views.xml',
        'views/school_leaves_views.xml',
        'wizad/school_report_wizard_views.xml',
        'report/club_template_report.xml',
        'report/school_report_action.xml',
        'views/school_exams_views.xml',
        'views/school_management_menus.xml',
    ],
    'installable': True,
    'application': True,
}
