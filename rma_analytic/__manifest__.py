# -*- coding: utf-8 -*-
# © 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Analytic Account in RMA",
    "version": "10.0.1.0.0",
    "author": "Eficent,"
              "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "website": "http://www.eficent.com",
    "category": "Analytic",
    "depends": ["rma", "analytic", "procurement_analytic",
                'stock_analytic_account'],
    "data": [
        "views/rma_order_line_view.xml"
    ],
    'installable': False,
}
