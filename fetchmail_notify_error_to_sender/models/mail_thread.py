
from odoo import api, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.model
    def message_route(
        self, message, message_dict, model=None, thread_id=None, custom_values=None
    ):
        try:
            res = super(MailThread, self).message_route(
                message,
                message_dict,
                model=model,
                thread_id=thread_id,
                custom_values=custom_values,
            )
        except ValueError as ve:
            fetchmail_server_id = self.env.context.get("default_fetchmail_server_id")
            if not fetchmail_server_id:
                raise ve
            fetchmail_server = (
                self.env["fetchmail.server"]
                .with_context({"sender_message": message, "route_exception": ve})
                .browse(fetchmail_server_id)
            )
            if not fetchmail_server.error_notice_template_id:
                raise ve
            fetchmail_server.error_notice_template_id.send_mail(fetchmail_server.id)
            raise ve
        return res
