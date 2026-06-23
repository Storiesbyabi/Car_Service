# -*- coding: utf-8 -*-
{
    'name': 'Limit Number of Open Task',
    'version': '1.0',
    'summary': 'Limit Number of Open Task',
    'description': """
     Limit Number of Open Task
     =================
     Used for importing sales order from excel
     """,
    'depends': [
        'base', 'project'
    ],
    'data': [
        'security/project_task_groups.xml',
        'views/res_user_views.xml',
        'wizard/partial_delivery.xml'

    ],
    'application': True,
}
