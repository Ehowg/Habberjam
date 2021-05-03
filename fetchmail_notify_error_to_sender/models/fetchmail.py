from odoo import fields, models


class FetchmailServer(models.Model):
    _inherit = "fetchmail.server"

    error_notice_template_id = fields.Many2one(
        "mail.template",
        string="Error notice template",
        help="Set here the template to use to send notice to sender when "
        "errors occur while fetching email",
    )
