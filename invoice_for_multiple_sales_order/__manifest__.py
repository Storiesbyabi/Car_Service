# -*- coding: utf-8 -*-
{
    'name':'Invoice for Multiple Sale Order',
'version': '1.0',
    'summary': 'Imported order Lines',
    'description': """
     Create new field in Invoice for
     selecting multiple sales order which are 
     not invoiced 
     """,
    'depends':[
        'base','account','sale_management'
    ],
    'data':[
        'views/invoice_so_views.xml',
    ],
    'application':True,
}