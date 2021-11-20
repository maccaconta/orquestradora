from api.utilities import fetchPOSTBasicAuth
from urllib.error import HTTPError


class ServiceEnviarAntecedente:

    @staticmethod
    async def serv_enviar_antecedente(param, service) -> dict:
        """
        nome: serv_enviar_antecedente
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        retorno_: dict = {}

        try:
            url_ = service.get("url") + "/atestadoAntecedentes/solicitacao/atestadoPorTipo/" + \
                   param["rg"] + "/" + param["digito"] + "/" + param["email"] + "/" + param["tipo"]

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
            retorno_ = await fetchPOSTBasicAuth(url_, {}, headers_, UserName_, password_)
            # print("Retorno da API:", retorno_)

        except HTTPError as e:
            print(e.read())

            retorno_ = {}

        return retorno_
