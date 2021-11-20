from api.utilities import fetchPOST
from urllib.error import HTTPError


class ServiceRebaixamentoCategoria:

    @staticmethod
    async def serv_rebaixamento_categoria(param, service) -> dict:
        """
        nome: serv_rebaixamento_categoria
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        retorno_: dict = {}
        print("CHEGUEEEEEEEEEI",param, service)
        try:
            url_ = service.get("url") + "/rebaixamento/" + \
                service.get("canal") + "/rebaixar/"

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
        