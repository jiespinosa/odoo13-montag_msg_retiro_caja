# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta


class location_inv(models.Model):
    _inherit = 'pos.config'

    segundos_msg = fields.Boolean(help="Manda mensaje al cajero para retirar caja")
