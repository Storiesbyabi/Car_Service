# # -*- coding: utf-8 -*-
{
'name': 'Add to Cart Qty',
    'version': '1.0',
    'summary': 'Add to Cart Qty',
    'description': """
     Add to Cart Qty in Web sale
     =================
     """,
    'depends': [
        'base','website','website_sale'],
    'data': [
'data/product_sale.xml'
    ],
    'assets':
        {
        'web.assets_frontend':[
            'add_to_cart_qty/static/src/css/product_sale.css'],
        },
'installable': True,
}