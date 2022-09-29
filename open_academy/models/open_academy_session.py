from odoo import models, fields


class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session"

    name = fields.Char(string="Session", required=True)
    start_date = fields.Date()
    duration = fields.Float()
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', ondelete="set null")
    course_id = fields.Many2one('openacademy.course', ondelete='')
