# TODO: Templates Positus
# https://docs.pt.posit.us/integracao/api#sticker
# https://docs.pt.posit.us/api-studio#message-templates
# from broadcast.whatsapp.whats_templates.generic import Generic
from broadcast.models import WhatsTemplate


class GetTemplate:

    def __init__(self):

        def get_template(template_type: str) -> dict:
            """
            fazer doc string
            """
            return WhatsTemplate.objects.get(type=template_type)

        def get_template2(template_type: str) -> dict:

            if template_type == "text":

                return {'to': "", 'type': "text", 'text': {'body': ""}}

            elif template_type == "option":

                return {'to': "",
                        'type': "interactive",
                        'recipient_type': "individual",
                        'interactive': {
                            'type': "button",
                            'header': {
                                'type': "text",
                                'text': ""
                            },
                            'body': {
                                'text': ""
                            },
                            'footer': {
                                "text": ""
                            },
                            'action': {
                                "buttons": []
                            }
                        }
                    }

            elif template_type == "link":

                return {'to': "",
                        'type': "text",
                        'text': {
                            "body": ""
                        },
                        'preview_url': True
                        }