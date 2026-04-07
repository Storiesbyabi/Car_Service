{
    'name':'Car Service',
    'depends':[
        'base','fleet','sale_management'
    ],
    'data':[
'views/car_service_menu.xml',
        'security/ir.model.access.csv',
        'views/car_service_user_details.xml',
        'views/car_service_quotation.xml'


    ],
    'application':True,
}