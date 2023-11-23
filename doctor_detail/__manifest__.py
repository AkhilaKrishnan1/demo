{
    'name': 'Doctor Details',
    'author': 'odoo',
    'website': 'www.odoo.com',
    'summary': 'odoo developer',
    'depends': ['base','product'],
    'data': {
        'security/ir.model.access.csv',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'data/doctor_sequence.xml',
        'data/patient_sequence.xml',
        'data/appointment_sequence.xml',
        'reports/patient_report.xml',
        'reports/patient_report_template.xml',
    }
}