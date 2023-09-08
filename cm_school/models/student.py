from odoo import api,models,fields

class Student(models.Model):
    _name = "school.student"
    _description = "Student Records"

    name = fields.Char(string='Name',required=True)
    age = fields.Integer(string='Age',reuired=True)
    gender = fields.Selection([("male","Male"),('female','Female'),('others','Others')],string='Gender')

    @api.model
    def _create(self, data_list):
        print('data____________________________',data_list)
        return super()._create(data_list)
