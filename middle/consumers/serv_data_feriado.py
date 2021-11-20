from api.utilities import fetchGETBasicAuth
from urllib.error import HTTPError


class ServiceDataFeriado:

    @staticmethod
    async def serv_data_feriado(param, service) -> dict:
        """
        nome: serv_data_feriado
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        retorno_: dict = {}
        
        try:
            url_ = service.get("url") + "/calendario/checarDataUtil/" + param["data"] + "/" + param["posto_id"]
                      
            headers_ = {
                'Content-Type': "application/json; charset=UTF-8",
             
            }
            print("Parâmetros da requisição proc0014:", param)

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
