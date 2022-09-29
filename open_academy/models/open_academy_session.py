from odoo import models, fields, api, exceptions
from datetime import timedelta


class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session"

    active = fields.Boolean(default=True)
    attendee_ids = fields.Many2many('res.partner')
    attendees_count = fields.Integer(
<<<<<<< HEAD
        compute='_compute_attendees_count',
        store=True
    )
    color = fields.Integer()
    course_id = fields.Many2one('openacademy.course')
=======
        string="Attendees count", compute='_compute_attendees_count', store=True)
    color = fields.Integer()
    course_id = fields.Many2one('openacademy.course')    
>>>>>>> main
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
<<<<<<< HEAD
    name = fields.Char(string="Session", required=True)
=======
    name = fields.Char(string="Session", required=True)    
>>>>>>> main
    seats = fields.Integer(string="Number of seats")
    start_date = fields.Date(default=fields.Date.today)
    taken_seats = fields.Float(compute='_compute_taken_seats')

    def _inverse_end_date(self):
        for record in self:
            if not (record.start_date and record.end_date):
                continue
<<<<<<< HEAD
=======
            
>>>>>>> main
            start_date = fields.Datetime.from_string(record.start_date)
            end_date = fields.Datetime.from_string(record.end_date)
            record.duration = (end_date - start_date).days + 1

    def _inverse_set_hours(self):
<<<<<<< HEAD
        for record in self:
            record.duration = record.hours / 24

    @api.depends('attendee_ids')
    def _compute_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendee_ids)

=======
        for r in self:
            r.duration = r.hours / 24

    @api.depends('attendee_ids')
    def _compute_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)
    
>>>>>>> main
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
<<<<<<< HEAD
        for record in self:
            record.hours = record.duration * 24
=======
        for r in self:
            r.hours = r.duration * 24
>>>>>>> main

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
<<<<<<< HEAD
                raise exceptions.ValidationError_("A session's instructor can't be an attendee.")
=======
                raise exceptions.ValidationError("A session's instructor can't be an attendee.")
>>>>>>> main

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value.",
                    'message': "The number of available seats may not be negative.",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees.",
                    'message': "Increase seats or remove excess attendees.",
                },
            }
<<<<<<< HEAD
=======

>>>>>>> main
