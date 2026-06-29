
{
    'name': 'Payment Provider: Paytrail',
    'version': '1.0',
    'category': 'Accounting/Payment Providers',
    'description': " ",  # Non-empty string to avoid loading the README file.
    'depends': ['payment'],
    'data': [
        'views/payment_provider_views.xml',
        'data/payment_provider_data.xml',
    ],
}
