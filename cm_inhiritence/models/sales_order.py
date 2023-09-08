from odoo import models, fields, api

class SalesOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users',String='Confirmed User')

    def action_confirm(self):
        print('sucess.......................')
        super(SalesOrder,self).action_confirm()
        self.confirmed_user_id = self.env.user.id
