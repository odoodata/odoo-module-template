from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

from . import constants


class Client(models.Model):
    _name = "gym.client"
    _description = "Gym Client"
    _order = "id desc"

    name = fields.Char(string='Nome', required=True, size=255, tracking=True)