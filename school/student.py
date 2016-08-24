from openerp import api, fields, models, _

class Student(models.Model):
    _name = "school.student"
    _description = "Student of School"
    
    name = fields.Char(required=True)