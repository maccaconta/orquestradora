from api.utilities import fetchPOST
from urllib.error import HTTPError


class ServiceConsultaRebaixamento:

    @staticmethod
    async def serv_consulta_rebaixamento(param, service) -> dict:
        """
        nome: serv_consulta_rebaixamento
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        retorno_: dict = {}
        print("",param)
        try:
            # url_ = service.get("url") + "/condutor/" + \
            #     service.get("canal") + "/atualiza-dados/"
            url_ = service.get("url") + "/rebaixamento/" + \
                service.get("canal") + "/consultar/"


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
        