from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description= "Courses"

    title = fields.Char(string = "Courses",required=True)
    description = fields.Text()

    responsible_user = fields.Many2one(comodel_name='res.users',ondelete="set null")

class Session(models.Model):
    _name = "openacademy.sessions"
    _description ="Sessions"

    name = fields.Char(string = "Sessions",required=True)
    start_date = fields.Date()
    duration=fields.Float()
    seats=fields.Integer(string="Number of seats")

    instructor = fields.Many2one(comodel_name='res.partner',ondelete="set null")