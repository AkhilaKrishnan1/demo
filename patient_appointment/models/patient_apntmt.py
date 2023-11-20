from odoo import fields, models, api

class PatientAppointment(models.Model):
    _name = 'patient.appointment'
    _rec_name = 'appointment_id'

    patient = fields.Char(string="Patient")
    age = fields.Char(string="age")
    appointment_id = fields.Char(string="Appointment Sequence", readonly=1)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    place = fields.Char(string="Place")
    doctor = fields.Many2one('doctor.doctor', string="Doctor")
    speciality = fields.Many2one('doctor.speciality', string="Speciality")
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")
    slot = fields.Many2one('time.slot', string="slot")
    date = fields.Date(string="Appointment Date")

    @api.model
    def create(self, vals):
        vals['appointment_id'] = self.env['ir.sequence'].next_by_code("patient.appointment.sequence")
        return super(PatientAppointment, self).create(vals)

class DoctorDoctor(models.Model):
    _name = 'doctor.doctor'

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    email = fields.Char(string="Email")
    license = fields.Char(string="License")

class DoctorSpeciality(models.Model):
    _name = 'doctor.speciality'
    _rec_name = 'speciality'

    speciality = fields.Char(string="Speciality")

class TimeSlot(models.Model):
    _name = 'time.slot'
    _rec_name = 'time_slot'

    time_slot = fields.Char(string="Time Slot")
