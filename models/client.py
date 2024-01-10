from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

from . import constants


class Client(models.Model):
    _name = "demo.client"
    _description = "Client"
    _order = "id desc"

    name = fields.Char(string='Name', required=True, size=40, tracking=True)
    age = fields.Integer(string='Age', required=True)