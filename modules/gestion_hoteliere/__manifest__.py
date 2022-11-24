# -*- coding: utf-8 -*-
{
    'name': 'Gestion Hotelière',
    'version': '1.0',
    "author": "El Houcine BRAHIM",
    "category": "Hotel Management",
    'description': """Module de base pour la gestion d'hotel""",
    'depends': [],
    'data': [
        # security
        "security/hotel_groups.xml",
        # data

        # views && actions
        "views/res_company.xml",
        "views/product_product.xml",
    ],
    'qweb': [],
    'demo': [],
    'test': [],
    'css': ["static/src/css/room_kanban.css"],
    'images': ["static/description/Hotel.png"],
    'application': True,
    'installable': True,
    'auto_install': False,
}

