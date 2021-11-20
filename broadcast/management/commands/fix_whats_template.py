from django.core.management.base import BaseCommand
from broadcast.models import WhatsTemplate


class Command(BaseCommand):
    """
             Name            : Command
            :param          : BaseCommand
            :create         : junho-2021
            description     : faz...
    ____________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    help = 'Valor default de templates do whatsapp'

    def handle(self, **options):
        """
        nome: handle
        :param options: str
        :return:
        """

        self.stdout.write('Criando dados Default do Templates do Whatsapp')

        # tamplete positus text
        WhatsTemplate.objects.create(type="text", template='{"to":"", "type": "text", "text": {"body": ""}}')

        # tamplete positus botões
        WhatsTemplate.objects.create(type="option", template='''{ "to": "",
                                                                  "type": "interactive",
                                                                  "recipient_type": "individual",
                                                                  "interactive": {
                                                                    "type": "button",
                                                                    "header": {
                                                                      "type": "text",
                                                                      "text": ""
                                                                    },
                                                                    "body": {
                                                                      "text": ""
                                                                    },
                                                                    "footer": {
                                                                      "text": ""
                                                                    },
                                                                    "action": {
                                                                      "buttons": []
                                                                    }
                                                                  }
                                                                }''')

        # tamplete positus text como URL
        WhatsTemplate.objects.create(type='link', template='''{ "to": "",
                                                                          "type": "text",
                                                                          "text": {
                                                                                "body": "" 
                                                                            },
                                                                            "preview_url": true
                                                                         }''')

        # tamplete positus Localização
        WhatsTemplate.objects.create(type='location', template='''{ "to": "",
                                                                    "type": "location",
                                                                    "location": {
                                                                        "longitude": "",
                                                                        "latitude": "",
                                                                        "name": "",
                                                                        "address": ""
                                                                    }
                                                                   }''')

        # tamplete positus documento pdf por link
        WhatsTemplate.objects.create(type='document', template='''{ "to": "", 
                                                                    "type": "document",
                                                                    "document": {
                                                                        "caption": "", 
                                                                        "link": "", 
                                                                        "filename": ""
                                                                    }
                                                                 }''')
        # WhatsTemplate.objects.create(template=)
        # WhatsTemplate.objects.create(template=)
        # WhatsTemplate.objects.create(template=)
        # WhatsTemplate.objects.create(template=)
        # WhatsTemplate.objects.create(template=)
        # WhatsTemplate.objects.create(template=)
        # WhatsTemplate.objects.create(template=)



