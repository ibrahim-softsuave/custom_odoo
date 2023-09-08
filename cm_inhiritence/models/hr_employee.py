from odoo import models, fields, api


class HrEmployeePrivate(models.Model):
    _inherit = "hr.employee"
    
    pan_card = fields.Char(string='PAN Card Number')
    ifc_code = fields.Char(string='IFC code')
