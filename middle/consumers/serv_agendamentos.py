from api.utilities import retryPUT2
from urllib.error import HTTPError


class ServiceAgendamentos:

    @staticmethod
    async def serv_agendamentos(param, service) -> dict:
        """
        nome: serv_agendamentos
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        retorno_: dict = {}
     
        try:
            url_ = service.get("url") + "/agendas"
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
            print(url_, headers_)
            return {}

        try:

            # retorno_ = await fetchPUT(url_, param, headers_)

            retorno_ = await retryPUT2(url_, param, headers_)
            print("Retorno da API PROC0008 :", retorno_)

        except HTTPError as e:
            print(e.read())
            
            retorno_ = {}

        return retorno_