# -*- coding: utf-8 -*-
# Copyright 2013 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale order revisions",
    "version": "10.0.1.0.1",
    "category": "Sale Management",
    "author": "Agile Business Group,"
              "Camptocamp,"
              "Akretion,"
              "Odoo Community Association (OCA), "
              "Serpent Consulting Services Pvt. Ltd.",
    "website": "http://www.agilebg.com",
    "license": "AGPL-3",
    "depends": [
        "sale",
    ],
    "data": [
        "view/sale_order.xml",
    ],
    "installable": True,
    "post_init_hook": "populate_unrevisioned_name",
}
