from middle.consumers.consumers import Consumers
from django.conf import settings
from common.utils import send_email


class Proc0010CertidaoNegativa(Consumers):

    async def get_certidao_negativa(request_) -> dict:
        """
         name: get_certidao_negativa
        :param request_: request
        :return: dict
        """

        data: dict = {}
        context_: dict = {}
        return_: dict = {}
        configs: dict = {}
        configs['subject'] = 'Certidão Negativa de Débitos'
        configs['name'] = str(request_["parameters"].get("proc0002_Nome", ""))
        configs['sender'] = settings.EMAIL_SENDER
        configs['receiver'] = str(request_["parameters"].get("proc0002_Email", ""))
        
        try:
            data = str(request_["parameters"].get("cpf", ""))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_certidao_negativa(data, request_["service"])
        # print(context_)
        if context_ == {} or not context_:
            return {
                "text": "api_erro",
                "context": {}
            }
        elif 'codigo' in context_ and context_['codigo'] == 401:
            return {
                "text": "api_nok",
                "context": context_
            }
        elif 'code' in context_:
            return {
                "text": "api_erro",
                "context": context_
            }
        else:
            try:
                send_email(configs, context_['arquivo'])

                return_ = {
                    'text': 'api_ok',
                    'context': {
                         "msg": "Certidão negativa de debitos enviada"
                    }
                }

            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': {}
                }

        return return_

