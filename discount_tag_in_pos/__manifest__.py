# -*- coding: utf-8 -*-
{
    'name': 'Discount Tag in POS',
    'version': '1.0',
    'summary': 'Discount Tag in POS',
    'description': """
     Discount Tag in POS
     =================
     Used for importing sales order from excel
     """,
    'depends': [
        'base','point_of_sale'
    ],
    'data': [
        'views/product_template_views.xml'
    ],
    'assets':{
      'point_of_sale._assets_pos': [
        'discount_tag_in_pos/static/src/js/discount_tag.js',
          'discount_tag_in_pos/static/src/css/discount_tag.css',
        'discount_tag_in_pos/static/src/xml/discount_tag.xml',
            'discount_tag_in_pos/static/src/js/order_line_discount.js',
      ],
    },
    'application': False,
}
