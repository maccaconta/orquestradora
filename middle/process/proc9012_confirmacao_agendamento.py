from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9012ConfirmacaoAgendamento(Consumers):

    async def getApiConfirmacaoAgendamento(request_) -> dict:
        """
        name: get_buscar_horario_agendamento_psicologico
        :param request_: request
        :return: dict
        """

        # Todo : não conseguimos ainda testar

        params_: dict = {}
        retorno_: dict = {}
        context_: dict = {}
        data_: dict = {}

        try:

            params_["cpf"] = request_["parameters"].get("cpf", 0)

            context_ = await Consumers.servConfirmacaoAgendamento(params_, request_["service"])

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        if context_ == {}:

            return {
                "text": "api_nok",
                "context": {}
            }

        else:

            context_tratado_: dict = {}
            context_tratado_ = splitDict("proc9012_", context_)

            cod_ = int(context_.get("codigo", 0))

            if cod_ == 400 or cod_ == 404:

                retorno_ = {
                    'text': 'api_erro',
                    'context': context_tratado_
                }

            else:

                retorno_ = {
                    'text': 'api_ok',
                    'context': context_tratado_
                }

        retorno_["context"]["process"] = ""

        return retorno_
