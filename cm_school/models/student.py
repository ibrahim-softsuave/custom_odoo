from odoo import api,models,fields

class Student(models.Model):
    _name = "school.student"
    _description = "Student Records"

    name = fields.Char(string='Name',required=True)
    age = fields.Integer(string='Age',reuired=True)
    gender = fields.Selection([("male","Male"),('female','Female'),('others','Others')],string='Gender')
    roll_number = fields.Char(string='Roll Number')

    @api.model
    def _create(self, data_list):
        data_list[0]['stored']['roll_number']=self.env['ir.sequence'].next_by_code('school.student') 
        return super()._create(data_list)
