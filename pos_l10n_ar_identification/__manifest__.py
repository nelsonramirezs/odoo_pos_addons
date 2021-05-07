# -*- coding: utf-8 -*-
#    Copyright (C) 2007  pronexo.com  (https://www.pronexo.com)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################## # 
# 
{
    'name': "PoS Add Fields to Add Customer view",

    'summary': """
        Adds Identification type field and AFIP Responsability type field to Client creation view.
    """,

    'description': """
        Adds Identification type field and AFIP Responsability type field to Client creation view.
    """,

    'author': "Pronexo",
    'website': "https://www.pronexo.com",

    'category': 'Sales/Point of Sale',
    'version': '1.0',
    'license': 'AGPL-3',

    'price': 29.00,
    'currency': 'USD',
    
    'depends': ['point_of_sale', 'l10n_latam_base','contacts'],

    'data': [
        'templates/point_of_sale_assets.xml',
    ],
    
    "qweb": [
        "static/src/xml/Screens/ClientDetailsEdit.xml"
    ],
    'images': ['static/description/banner.png'],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}
