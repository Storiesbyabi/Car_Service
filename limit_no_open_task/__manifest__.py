# -*- coding: utf-8 -*-
{
    'name': 'Limit Number of Open Task',
    'version': '1.0',
    'summary': 'Limit Number of Open Task',
    'description': """
     Limit Number of Open Task
     =================
     Used for importing sales order from exel
     """,
    'depends': [
        'base', 'project'
    ],
    'data': [
'security/project_task_groups.xml',
        'security/ir.model.access.csv',
        'views/project_approve_views.xml',
        'views/res_user_views.xml',
        'views/project_task_views.xml',
        'views/project_menu_items.xml'

    ],
    'application': True,
}
