# -*- coding: utf-8 -*-
{
    'name':'Import Order lines',
'version': '1.0',
    'summary': 'Imported order Lines',
    'description': """
     Sales Order Line
     =================
     Used for importing sales order from exel
     """,
    'depends':[
        'base','sale_management'
    ],
    'data':[
      'security/ir.model.access.csv',
        'wizard/add_orderline_wizard.xml',
        'views/sale_order_views.xml',

    ],
    'application':True,
}