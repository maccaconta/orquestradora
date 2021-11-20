from api.utilities import fetchGETBasicAuth
from urllib.error import HTTPError


class ServiceRestricaoAAC:

    @staticmethod
    async def serv_restricao_aac(param, service) -> dict:
        """
        nome: serv_restricao_aac
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        retorno_: dict = {}

        try:
            url_ = service.get("url") + "/atestadoAntecedentes/solicitacao/" + param["rg"] + "/" + param["digito"] + "/" + \
                        param["DataNascimento"] + "/" + param["cpf"] + "/" + \
                            param["ip"] + "/" + param["session"] + "/" + param["proc0002_Id"]
            headers_ = {
                'Content-Type': "application/json; charset=UTF-8",
                'Cache-Control': "no-cache",
                'Accept': "*/*",
                'Connection': "keep-alive"
            }
            print("Parâmetros da requisição:", param)

            UserName_ = service["username"]
            password_ = service["password"]

        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)
            return {}

        try:
            retorno_ = await fetchGETBasicAuth(url_, {}, headers_, UserName_, password_)
            print("Retorno da API:", retorno_)

        except HTTPError as e:
            print(e.read())

            retorno_ = {}

        return retorno_
