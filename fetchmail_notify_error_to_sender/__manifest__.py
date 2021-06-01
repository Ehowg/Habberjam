# Copyright 2015 Lorenzo Battistini <lorenzo.battistini@agilebg.com>
{
    "name": "Fetchmail Notify Error to Sender",

    "summary": "If fetching mails gives error, send an email to sender",

    "version": "14.0",

    "category": "Tools",

    "author": "TraceNcode Technologies Pvt. Ltd.",

    "website": "https://tracencode.com",

    "license": "AGPL-3",

    "depends": ["base", "fetchmail"],

    "data": ["views/fetchmail_view.xml", "data/email_template_data.xml"],

    "qweb": [],

    "installable": True,
    
    "application": False,
}
