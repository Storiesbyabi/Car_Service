# -*- coding: utf-8 -*-
{
    'name': 'Create POS Order From Sales',
    'version': '1.0',
    'description': """
     Create POS Order From Sales
     =================
     """,
    'depends': [
        'base','sale_management','point_of_sale',
    ],
    'data': [
'security/ir.model.access.csv',
        'views/sale_order_form_views.xml',
        'wizard/pos_wizard_views.xml',

    ],
    'application': True,
}
