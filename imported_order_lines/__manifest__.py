# -*- coding: utf-8 -*-
{
    'name':'Import Order lines',
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