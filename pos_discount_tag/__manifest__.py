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
        'base', 'point_of_sale'
    ],
    'data': [
        'views/product_template_views.xml',
        'views/res_partner_views.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_discount_tag/static/src/js/customer_account.js',
            'pos_discount_tag/static/src/js/order_line_discount.js',
            'pos_discount_tag/static/src/js/partner.js',
            'pos_discount_tag/static/src/js/discount_tag.js',
            'pos_discount_tag/static/src/css/discount_tag.css',
            'pos_discount_tag/static/src/xml/discount_tag.xml',
            'pos_discount_tag/static/src/xml/customer_account.xml',

        ],
    },
    'application': False,
}
