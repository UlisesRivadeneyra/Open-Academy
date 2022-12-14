from odoo import models, fields


class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = 'Register attendees'

    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    session_id = fields.Many2one(
        'openacademy.session',
        required=True,
        default=lambda self: self._default_session_id()
    )

    def _default_session_id(self):
        return self.env['openacademy.session'].browse(self._context.get('active_id'))

    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
