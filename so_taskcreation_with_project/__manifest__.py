# -*- coding: utf-8 -*-
{
    'name': 'Sales Order Task Creation with Project',
    'version': '1.0',
    'summary': 'Sales Order Task Creation with Project',
    'description': """
     Sales Order Task Creation with Project
     =================
     Used for importing sales order from excel
     """,
    'depends': [
        'base', 'sale','sale_management','project',
    ],
    'data': [
        'views/sale_order_form_views.xml'
    ],
    'application': True,
}
