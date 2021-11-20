from api.utilities import fetchPOST
from urllib.error import HTTPError


class ServiceEncontrarProcessos:

    @staticmethod
    async def serv_encontrar_processos(param, service) -> dict:
        """
        nome: serv_enviar_token
        :return: ...
        """

        url_: str = ""
        header_: dict = {}
        retorno: dict = {}

        try:
            url_ = service.get("url") + "/cumprimento-suspensao/" + \
                service.get("canal") + "/buscar-portarias-suspensao/"
            headers_ = {
                'Authorization': "Bearer " + service.get("token"),
                'Cache-Control': "no-cache",
                'Content-Type': "application/json",
                'Accept': "*/*",
                'Connection': "keep-alive"
            }

            print("Parâmetros da requisição:", param)

        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)
            return {}

        try:
            retorno_ = await fetchPOST(url_, param, headers_)
            print("Retorno da API:", retorno_)

        except HTTPError as e:
            print(e.read())
            
            retorno_ = {}

        return retorno_
        