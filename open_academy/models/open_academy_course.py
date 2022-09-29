from odoo import models, fields


class Course(models.Model):
    _name = "openacademy.course"
    _description = "Course"

    title = fields.Char(string="Course", required=True)
    description = fields.Text()

    responsible_user = fields.Many2one("res.users", ondelete="set null")
