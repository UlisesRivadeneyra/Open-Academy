from odoo import models, fields, api, exceptions
from datetime import timedelta


class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session"

    name = fields.Char(string="Session", required=True)
    start_date = fields.Date()
    duration = fields.Integer()
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one(
        'res.partner',
        ondelete="set null",
        domain=[
            '|',
            ('instructor', '=', True),
            ('category_id.name', 'ilike', "Teacher")
        ]
    )
    course_id = fields.Many2one('openacademy.course')
    attendee_ids = fields.Many2many('res.partner')
    taken_seats = fields.Float(compute='_compute_taken_seats')
    start_date = fields.Date(default=fields.Date.today)
    active = fields.Boolean(default=True)
    end_date = fields.Date(
        store=True,
        compute='_compute_get_end_date',
        inverse='_inverse_set_end_date'
    )

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
                continue
            start = fields.Datetime.from_string(record.start_date)
            duration = timedelta(days=record.duration, seconds=-1)
            record.end_date = start + duration

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for record in self:
            if record.instructor_id in record.attendee_ids:
                raise exceptions.ValidationError_("A session's instructor can't be an attendee")

    def _set_end_date(self):
        for record in self:
            if not (record.start_date and record.end_date):
                continue

            start_date = fields.Datetime.from_string(record.start_date)
            end_date = fields.Datetime.from_string(record.end_date)
            record.duration = (end_date - start_date).days + 1
