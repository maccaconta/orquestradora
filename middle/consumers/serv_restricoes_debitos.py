from api.utilities import fetchPOST
from urllib.error import HTTPError


class ServiceRestricoesDebitos:

    @staticmethod
    async def serv_restricoes_debitos(param, service) -> dict:
        """
        nome: serv_restricoes_debitos
        :return: ...
        """

        url_: str = ""
        header_: dict = {}
        retorno: dict = {}

        try:
            url_ = service.get("url") + "/consultas/" + \
                service.get("canal") + "/multas-debitos/"

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
        
  