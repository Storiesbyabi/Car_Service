# # -*- coding: utf-8 -*-
{
    'name':'School Management',
    'version':'1.0',
    'summary':'School management for school',
    'description':"""
     School management
     =================
     Used for managing the records of students in school
     """,
    'category':'SchoolManagement/SchoolManagement',
    'depends':[
        'base','mail'],
    'data':[
        'data/ir_sequence_data.xml',
        'data/school_class.xml',
        'data/school_department.xml',
        'data/school_subject.xml',
'security/ir.model.access.csv',
'views/school_department_view.xml',
        'views/school_registration_view.xml',
        'wizad/school_registration_wizard_view.xml',
        'views/school_students_view.xml',
        'views/school_class_view.xml',
'views/school_subject_view.xml',
        'views/school_academic_year_view.xml',
        'views/school_management_menus.xml',
    ],
    'installable':True,
    'application':True,
}
