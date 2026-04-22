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
        'base','mail'
    ],
    'data':[
        'data/ir_sequence_data.xml',
'security/ir.model.access.csv',
'views/school_department.xml',
        'views/school_registration.xml',
        'views/school_class.xml',
'views/school_subject.xml',
        'views/school_academic_year.xml',
        'views/school_management_menus.xml',
    ],
    'demo':[
        'demo/demo_data.xml'
    ],
    'installable':True,
    'application':True,
}
