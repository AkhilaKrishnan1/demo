from odoo import fields, models, api

class PatientDetails(models.Model):
    _name = 'patient.details'

    name = fields.Char(string="Name")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    code_id = fields.Char(string="Code", readonly=1)
    image = fields.Binary()
    age = fields.Char(string="Age")
    dob = fields.Char(string="Date Of Birth")
    doctor = fields.Many2one('doctor.details', string="Doctor")
    address = fields.Char(string="Address")
    street2 = fields.Char(string="Street2")
    city = fields.Char(string="city")
    state_ids = fields.Many2one('res.country.state', string="state")
    zip = fields.Char(string="zip")
    country_ids = fields.Many2one('res.country', string="country")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    marital = fields.Selection([('married', 'Married'), ('single', 'Single')], string="Marital Status")
    height = fields.Char(string="Height")
    weight = fields.Char(string="Weight")
    temp = fields.Char(string="Temp")
    rbs = fields.Char(string="RBS")
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count")

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['appointment.details'].search_count([('patient_ids', '=', rec.ids)])
            rec.appointment_count = appointment_count

    @api.model
    def create(self, vals):
        vals['code_id'] = self.env['ir.sequence'].next_by_code("patient.details.sequence")
        return super(PatientDetails, self).create(vals)

    def action_open_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'appointment.details',
            'view_mode': 'tree,form',
            'domain': [('patient_ids', '=', self.ids)],
            'target': 'current'
        }
