from odoo import models, fields, api, exceptions, _
from datetime import timedelta


class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session"

    active = fields.Boolean(default=True)
    attendee_ids = fields.Many2many('res.partner')
    attendees_count = fields.Integer(
        string="Attendees", compute='_compute_attendees_count', store=True)
    color = fields.Integer()
    course_id = fields.Many2one('openacademy.course')
    duration = fields.Integer()
    end_date = fields.Date(
        store=True,
        compute='_compute_end_date',
        inverse='_inverse_end_date'
    )
    hours = fields.Float(string="Duration in hours",
                         compute='_compute_get_hours', inverse='_inverse_set_hours')
    instructor_id = fields.Many2one(
        'res.partner',
        ondelete="set null",
        domain=[
            '|',
            ('instructor', '=', True),
            ('category_id.name', 'ilike', "Teacher")
        ]
    )
    name = fields.Char(string="Session", required=True)
    seats = fields.Integer(string="Number of seats")
    start_date = fields.Date(default=fields.Date.today)
    taken_seats = fields.Float(compute='_compute_taken_seats')

    def _inverse_end_date(self):
        for record in self:
            if not (record.start_date and record.end_date):
                continue

            start_date = fields.Datetime.from_string(record.start_date)
            end_date = fields.Datetime.from_string(record.end_date)
            record.duration = (end_date - start_date).days + 1

    def _inverse_set_hours(self):
        for record in self:
            record.duration = record.hours / 24

    @api.depends('attendee_ids')
    def _compute_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendee_ids)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
                continue
            start = fields.Datetime.from_string(record.start_date)
            duration = timedelta(days=record.duration, seconds=-1)
            record.end_date = start + duration

    @api.depends('duration')
    def _compute_get_hours(self):
        for record in self:
            record.hours = record.duration * 24

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * (len(record.attendee_ids) / record.seats)

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for record in self.filtered('instructor_id'):
            if record.instructor_id in record.attendee_ids:
                raise exceptions.ValidationError(_("A session's instructor can't be an attendee."))

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Incorrect 'seats' value."),
                    'message': _("The number of available seats may not be negative."),
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': _("Too many attendees."),
                    'message': _("Increase seats or remove excess attendees."),
                },
            }
