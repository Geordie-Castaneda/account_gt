from odoo import api, fields, models, tools, _
from odoo.modules import get_module_resource

# Prueba
class Partner(models.Model):
    _inherit = "res.partner"

    pequenio_contribuyente = fields.Boolean('Pequeño contribuyente')
