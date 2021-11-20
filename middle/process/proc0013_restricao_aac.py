from middle.consumers.consumers import Consumers
from common.utils import Formatted


class Proc0013RestricaoAAC(Consumers):

    async def get_restricao_aac(request_) -> dict:
        """
         name: get_restricao_aac
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            params_["rg"] = str(request_["parameters"].get("proc0002_RG", ""))
            params_["digito"] = str(request_["parameters"].get("proc0002_digito", ""))
            params_["DataNascimento"] = Formatted(str(request_["parameters"].get("proc0002_DataNascimento", "")))
            params_["cpf"] = str(request_["parameters"].get("proc0002_cpf", ""))
            params_["proc0002_Id"] = str(request_["parameters"]["proc0002_Id"])
            params_["session"] = str(request_["parameters"]["proc0002_Id"])
            params_["ip"] = "10.9.9.10"

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_restricao_aac(params_, request_["service"])

        if context_ == {}:
            return {
                "text": "api_nok",
                "context": context_
            }
        else:
            context_["process"] = ""
            return_ = {
                'text': 'api_ok',
                'context': context_

            }
        return return_
