from odoo import fields, models, api


class AppointmentDetails(models.Model):
    _name = 'appointment.details'
    _rec_name = 'name_id'

    name_id = fields.Char(string="Name", readonly=1)
    patient_ids = fields.Many2one('patient.details', string="Patient")
    age = fields.Char(string="Age")
    doctor_ids = fields.Many2one('doctor.details', string="Doctor")
    clinic_ids = fields.Many2one('doctor.clinic', string="Clinic")
    date = fields.Date(string="Date")
    time = fields.Float(string="Time")
    product_ids = fields.One2many('appointment.service', 'product_id', string="products")

    @api.model
    def create(self, vals):
        vals['name_id'] = self.env['ir.sequence'].next_by_code("appointment.details.sequence")
        return super(AppointmentDetails, self).create(vals)

class AppointmentService(models.Model):
    _name = 'appointment.service'

    product_id = fields.Many2one('appointment.details', invisible=True)
    prdt_id = fields.Many2one('product.product', string="product", domain="[('type', '=', 'service')]")
    product_qunty = fields.Float(string="Product Quantity")



#domain="[('type', '=', 'service')]"