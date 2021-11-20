from api.utilities import fetchPOSTBasicAuth
from urllib.error import HTTPError
from common.rg_validator import ValidaRg


validatorRg: ValidaRg = ValidaRg()


class ServiceAntecedentesCriminais:

    @staticmethod
    async def serv_antecedentes_criminais(param, service) -> dict:
        """
        nome: serv_antecedentes_criminais
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        retorno_: dict = {}
        _rg: str = ""

        try:
            url_ = service.get("url") + "/atestadoAntecedentes/solicitacao/download/" + \
                   param["rg"] + "/" + param["digito"]

            headers_ = {
                'Content-Type': "application/json; charset=UTF-8",
                'Cache-Control': "no-cache",
                'Accept': "*/*",
                'Connection': "keep-alive"
            }
            print("Parâmetros da requisição:", param)

            UserName_ = service["username"]
            password_ = service["password"]

            _rg = str(param["rg"]) + str(param["digito"])       
            validatorRg.set_rg(_rg)
           
            if validatorRg.valida_rg():
                retorno_ = await fetchPOSTBasicAuth(url_, {}, headers_, UserName_, password_)
                # print("Retorno da API:", retorno_)
            else:
                return {'code': 500,
                        'Mensagem': 'RG inválido'
                        }
        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)
            return {}

        return retorno_
