from odoo import api, models,fields


class BirthdayReminder(models.AbstractModel):
    _name = 'birthday.reminder'

    @api.model
    def send_birthday_mail(self):
        # Search for employees whose birthday is coming up
        employees = self.env['hr.employee'].search([('birthday', '=', fields.Date.today())])
        # Send email to each employee
        for employee in employees:
            template = self.env.ref('Experiment.email_Birthday_reminder_template')
            template.send_mail(employee.id, force_send=True)


