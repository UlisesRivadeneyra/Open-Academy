from odoo import models, fields


class Course(models.Model):
    _name = "openacademy.course"
    _description = "Course"

<<<<<<< HEAD
    title = fields.Char(string="Course name", required=True)
    description = fields.Text(string="Description of the course")
    responsible_user_id = fields.Many2one(
        "res.users",
        ondelete="set null",
        string="Resonsible of the course"
    )
=======
    title = fields.Char(string="Course", required=True)
    description = fields.Text()
    responsible_user_id = fields.Many2one("res.users", ondelete="set null")
>>>>>>> main
    session_ids = fields.One2many(
        "openacademy.session", inverse_name="course_id")

    _sql_constraints = [
        (
            'name_description_check',
            'CHECK(title != description)',
            "The title of the course should not be the same that description."
        ),
        ('name_unique', 'UNIQUE(title)', "The course title must be unique."),
    ]

    def copy(self, default=None):
        default = dict(default or {})
        default.update({'title': f"Copy of {self.title}"})
        return super().copy(default)
