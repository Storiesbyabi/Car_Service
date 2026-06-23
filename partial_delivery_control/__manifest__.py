# # -*- coding: utf-8 -*-
{
'name': 'Partial Delivery Control with Approval',
    'version': '1.0',
    'summary': 'Partial Delivery Control with Approval',
    'description': """
     Partial Delivery Control with Approval
     =================
     """,
    'depends': [
        'base','stock'],
    'data': [
        'security/approval_request_security.xml',
        'views/stock_picking.xml',
        'views/product_product_views.xml',
        'wizard/partial_delivery.xml'
    ],
'installable': True,
}