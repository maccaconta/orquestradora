from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9037GravarDadosCidadao(Consumers):

    async def setGravarDadosCidadao(request_) -> dict:
        """
        name: setGravarDadosCidadao
        :param request_: request
        :return: dict
        """

        # Todo : não conseguimos ainda testar

        retorno_: dict = {}
        context_: dict = {}
        data_: dict = {}

        params_: dict = {
            'cidadao': {
                'autoriza_envio_email': True,
                'autoriza_envio_sms': True,
                'celular': '',
                'cpf': 0,
                'ddd_celular': '',
                'ddd_telefone': '',
                'email': '',
                'necessidade_veiculo_adaptado': False,
                'nome': '',
                'pretende_atividade_remunerada': False,
                'telefone': ''
              }
        }

        try:

            params_["cidadao"]["autoriza_envio_email"] = True \
                if str(request_["parameters"].get("autoriza_email", "SIM")).upper() == "SIM" \
                else False

            params_["cidadao"]["autoriza_envio_sms"] = True \
                if str(request_["parameters"].get("autoriza_sms", "SIM")) == "SIM" \
                else False

            telefone = str(request_["parameters"].get("numero_telefone"))
            celular = str(request_["parameters"].get("ddd_celular", ""))
            dddtel = telefone[:2]
            numtel = telefone[2:]
            dddcel = celular[:2]
            numcel = celular[2:]
            
            params_["cidadao"]["celular"] = numcel

            params_["cidadao"]["cpf"] = int(request_["parameters"].get("cpf", ""))

            params_["cidadao"]["ddd_celular"] = dddcel

            params_["cidadao"]["ddd_telefone"] = dddtel

            params_["cidadao"]["email"] = request_["parameters"].get("email", 0)

            params_["cidadao"]["necessidade_veiculo_adaptado"] = True \
                if str(request_["parameters"].get("necessidade_veiculo_adaptado", "SIM")).upper() == "SIM" \
                else False

            params_["cidadao"]["nome"] = str(request_["parameters"].get("nome", ""))

            params_["cidadao"]["pretende_atividade_remunerada"] = True \
                if str(request_["parameters"].get("pretende_atividade_remunerada", "SIM")).upper() == "SIM" \
                else False

            params_["cidadao"]["telefone"] = numtel

            context_ = await Consumers.servGravarDadosCidadao(params_, request_["service"])

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)


        if context_ == {}:

            return {
                "text": "api_nok",
                "context": {}
            }

        else:

            context_tratado_: dict = {}
            context_tratado_ = splitDict("proc9037_", context_)

            cod_ = int(context_.get("codigo", 0))
            if cod_ == 0:

                retorno_ = {
                    'text': 'api_ok',
                    'context': context_tratado_
                }
            else:
                retorno_ = {
                    'text': 'api_erro',
                    'context': context_tratado_
                }

        retorno_["context"]["process"] = ""

        return retorno_
