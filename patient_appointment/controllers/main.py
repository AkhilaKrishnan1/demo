from odoo import http
from odoo.http import request

class DrAppointment(http.Controller):
    @http.route('/doctor_appointment', type="http", auth="public", website=True)
    def doctor_appointment(self, **kw):
        doctor_rec = request.env['doctor.doctor'].sudo().search([])
        print("doc", doctor_rec)
        speciality_rec = request.env['doctor.speciality'].sudo().search([])
        print("spec", speciality_rec)
        slot_rec = request.env['time.slot'].sudo().search([])
        return request.render('patient_appointment.dr_appointment', {
            'doctor_rec': doctor_rec,
            'speciality_rec': speciality_rec,
            'slot_rec': slot_rec
        })

    @http.route('/create/doctor', type="http", auth="public", website=True)
    def doctor(self, **kw):
        print("uuuuu", kw)
        request.env['patient.appointment'].sudo().create(kw)
        return http.request.render('patient_appointment.thanks_page', {})
