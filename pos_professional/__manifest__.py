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
	"name" : "POS Professional",
	"version" : "14.7.1.1",
	"category" : "Point of Sale",
	'summary': 'POS Professional (Reimprimir tickets, Cupón Descuento, Notas de crédito, Mostrar Stock, Cargos por bolsa, importación presupuestos, crear presupuestos, contar items)',
	"description": """

	OS Professional (Reimprimir tickets, Cupón Descuento, Notas de crédito, Mostrar Stock, Cargos por bolsa, importación presupuestos, crear presupuestos, contar items)

	""",
	"author": "Pronexo",
	"depends" : ['base','sale_management','account','point_of_sale'],
	"price": 69,
	"currency": 'EUR',
	"website" : "https://www.pronexo.com",
	"data": [
		'security/ir.model.access.csv',
		'data/data.xml',
		'views/assets.xml',
		'views/pos_config_view.xml',
		'views/pos_order_view.xml',
		'views/account_view.xml',
		'views/pos_gift_coupon.xml',
		'views/report_pos_gift_coupon.xml',
	],
	'qweb': [
		'static/src/xml/pos_orders_list.xml',
		'static/src/xml/reorder_reprint_return.xml',
		'static/src/xml/sale_orders.xml',
		'static/src/xml/pos_bag_charges.xml',
		'static/src/xml/item_count.xml',
		'static/src/xml/pos_discount.xml',
		'static/src/xml/pos_stock.xml',
		'static/src/xml/gift_coupon_voucher.xml',
	],
	"auto_install": False,
	"installable": True,
	"images":['static/description/Banner.png'],
	"live_test_url":'https://youtu.be/cbgN3yzZS1U',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
