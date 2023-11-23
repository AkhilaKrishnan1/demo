from odoo import fields, models, api


class DoctorDetail(models.Model):
    _name = 'doctor.details'

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    image = fields.Binary()
    education_ids = fields.Many2many('education.details', string="Education")
    doctor_id = fields.Char("Doctor id", readonly=1)
    license = fields.Char(string="License")
    speciality_ids = fields.Many2one('speciality.details', string="Speciality")
    consultation_id = fields.Many2one('product.product', string="Consultation Service", domain="[('type', '=', 'service')]")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    hospital_ids = fields.Many2many('hospital.list', string="Hospital")
    address = fields.Char(string="Address")
    street2 = fields.Char(string="Street2")
    city = fields.Char(string="city")
    state_ids = fields.Many2one('res.country.state', string="state")
    zip = fields.Char(string="zip")
    country_ids = fields.Many2one('res.country', string="country")
    appointment_count = fields.Integer(string="Appointment Count", compute="_compute_appointment_count")
    patient_count = fields.Char(string="Patient", compute="_compute_patient_count")

    def _compute_patient_count(self):
        for rec in self:
            patient_count = self.env['patient.details'].search_count([('doctor', '=', rec.ids)])
            rec.patient_count = patient_count

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['appointment.details'].search_count([('doctor_ids', '=', rec.ids)])
            rec.appointment_count = appointment_count

    def action_smart_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'appointment.details',
            'view_mode': 'tree,form',
            'domain': [('doctor_ids', '=', self.ids)],
            'target': 'current'
        }

    @api.model
    def create(self, vals):
        vals['doctor_id'] = self.env['ir.sequence'].next_by_code("doctor.details.sequence")
        return super(DoctorDetail, self).create(vals)

class EducationDetails(models.Model):
    _name = 'education.details'
    _rec_name = 'education'

    education = fields.Char(string="Education")

class SpecialityDetails(models.Model):
    _name = 'speciality.details'
    _rec_name = 'speciality'

    speciality = fields.Char(string="Speciality")

class HospitalList(models.Model):
    _name = 'hospital.list'
    _rec_name = 'hospital'

    hospital = fields.Char(string="Hospital")


class DoctorSchedule(models.Model):
    _name = 'doctor.schedule'
    _rec_name = 'name2'

    name2 = fields.Char(string="Name")
    doctor_ids = fields.Many2one('doctor.details', string="Doctor")
    company_ids = fields.Many2one('res.company', string="Company")
    clinic_ids = fields.Many2one('doctor.clinic', string="Clinic")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")

class DoctorClinic(models.Model):
    _name = 'doctor.clinic'
    _rec_name = 'clinic'

    clinic = fields.Char(string="Clinic")
