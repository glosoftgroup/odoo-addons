# -*- coding: utf-8 -*-

from odoo import models, fields, api


class XtendProductTemplate(models.Model):
	_inherit = 'product.template'

	# Add a new column to the product.template model, by default partners are not
	# extended_field
	extended_field = fields.Char(default=False)# -*- coding: utf-8 -*-
