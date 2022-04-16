# -*- coding: utf-8 -*-
{
    'name': "MONTAG-MSG_RETIRO_CAJA",

    'summary': """
        mensaje al cajero para que retire caja cada n segundos""",

    'description': """
        modificaciones de point of sale
    """,

    'author': "Consultoria Montag MEXICO",
    'website': "consultoriamontag.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Point of sale',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'pos_sale'],

    # always loaded
    'data': [
            'views/templates.xml',

    ],

}
