{
    'name': 'Patient Appointments',
    'author': 'odoo',
    'website': 'www.odoo.com',
    'summary': 'odoo developer',
    'depends': ['base','website'],
    'data': {
        'security/ir.model.access.csv',
        'views/patient_apntmnt_view.xml',
        'views/dr_appointment_menu.xml',
        'views/template.xml',
        'data/apntmnt_sequence.xml',
    }
}