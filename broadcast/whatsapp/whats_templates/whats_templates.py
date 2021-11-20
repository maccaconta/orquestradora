# TODO: Templates Positus
# https://docs.pt.posit.us/integracao/api#sticker
# https://docs.pt.posit.us/api-studio#message-templates
from asgiref.sync import sync_to_async
from broadcast.models import WhatsTemplate
from broadcast.serializers import TemplateSerializer


class WhatsTemplates(TemplateSerializer):  # TODO: mover métodos para GetTemplate e herdar aqui

    def __init__(self):
        super(WhatsTemplates, self).__init__()

    async def getTemplate(self, template_type: str) -> dict:  # TODO mover para classe GetTemplate

        """
        ------------------------------
        get_template: recupera de forma assincrona o template
                       apropriado para o tipo de mensagem do whatsapp
        :param: template_type: str
        :return: dict

        ------------------------------
        """

        # template_ = await sync_to_async(WhatsTemplate.objects.get)(type=template_type)
        # serial_ = await self.template_serializer(template_)
        #
        # return serial_

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

    async def templateMount(self, number: str, data: dict, data_send: dict) -> dict:
        # recebe tipo (text) e assim seta o montador de template customizado
        # data contem o retorno da watson e informações que vão ser usadas para montar os templates
        """
            fazer doc string
        """
        isBotaoTexto:bool = False

        # print(f'___ORCHEST to WHATS: {data}')

        try:
            isBotaoTexto = True if len(data['option']['select']['options']) > 3 else False
        except:
            isBotaoTexto = False

        # Template do tipo texto

        if data['type'] == 'text':

            template = await self.getTemplate(data['type'])
            template['to'] = number
            template['text']['body'] = data['text'] + sticker(data['text'])

            return template

        elif data['type'] == 'option' and isBotaoTexto:
            template = await self.getTemplate('text')
            template['to'] = number

            texto = data['option']['select']['title'] + sticker(data['text']) + "\n"

            for i, label in enumerate(data['option']['select']['options']):
                texto += f"{i+1} - {label['label']}" + "\n"

            template['text']['body'] = texto

            return template

        # template do tipo botões
        elif data['type'] == 'option' and not isBotaoTexto:
            template = await self.getTemplate(data['type'])

            title_ = data['option']['select']['title'] or "Menu"

            template['to'] = number
            template['type'] = 'interactive'
            template['interactive']['header']['text'] = title_[0:50] # "escolha uma opção"
            template['interactive']['body']['text'] = "    opções" # data['text'] if data['text'] else '---'
            template['interactive']['footer']['text'] = ''

            for i, opcao in enumerate(data['option']['select']['options']):

                if i == 3:
                    break

                data = {
                    "type": "reply",
                    "reply": {
                        "id": f"unique-postback-id-{opcao['value']['input']['text']}",
                        "title": f"{opcao['label'][0:19]}"
                    }
                }

                template['interactive']['action']['buttons'].append(data)

                # print(template)

            return template  # retornar template montado com os valores

        # template do tipo texto com URL
        elif data['type'] == 'link':

            template = await self.getTemplate(data['type'])

            template['to'] = number
            template['text']['body'] = data['link']

            return template  # retornar template montado com os valores

        # template do tipo localização
        elif data['type'] == 'location':

            template = self.getTemplate(data['type'])

            template['to'] = number
            # template['type'] = data['type']
            template['location']['longitude'] = data['location']['longitude']
            template['location']['latitude'] = data['location']['latitude']
            template['location']['name'] = data['location']['name']
            template['location']['address'] = data['location']['address']

            return template  # retornar template montado com os valores

        # template do tipo url para documento pdf
        elif data['type'] == 'document':

            template = self.getTemplate(data['type'])
            template['to'] = number
            template['document']['link'] = data['document']['link']
            template['document']['filename'] = data['document']['filename']

            return template # retornar template montado com os valores

        # template do tipo text para upload de documentos
        elif data['type'] == 'upload':

            template = await self.getTemplate('text')
            template['to'] = number
            template['text']['body'] = f'{data["text"]} \n {", ".join(data["upload"])}.'

            return template  # retornar template montado com os valores

        # template do tipo document para download de documento
        elif data['type'] == 'download':
            template = await self.getTemplate('document')
            template['to'] = number
            template['document']['caption'] = 'Prodesp document'
            template['document']['link'] = data['link']
            template['document']['filename'] = 'document.pdf' #TODO colocar nome do documento dinamico extraido do link

            return template  # retornar template montado com os valores

        elif data['type'] == 'login':

            template = await self.getTemplate('link')

            url_ = " http://3a71-2804-14d-3282-5591-bc6c-ddbe-34e4-77c6.ngrok.io/orchest/v1/loginsp/"
            template['to'] = number
            template['text']['body'] = url_ + "?id=" + number[1:]

            return template  # retornar template montado com os valores


def sticker(texto):
    nomes = ['olá', 'skill', 'cpf', 'desenvolvimento', 'obrigado','link', 'veiculo', "opções","menu", "serviço","felizes"]

    stickers = ["🇧🇷 ⭐😃⭐ 🇧🇷", "🚀", "✨✨✨", "⚠️", "❤️❤️❤️", "🆗 ", "🚗", "🟢 🔴 🟡", "⭐", "✨😃✨","😃😃"]
    
    lowertext = texto.lower()

    for i in range(len(nomes)):
            if nomes[i] in lowertext:
                return stickers[i]

    return ""




