from odoo import api, fields, models, tools, _
from odoo.modules import get_module_resource

# Test
# Test2
class Partner(models.Model):
    _inherit = "res.partner"

    pequenio_contribuyente = fields.Boolean('Pequeño contribuyente')
