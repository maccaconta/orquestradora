from api.utilities import fetchPOST
from urllib.error import HTTPError


class ServiceConsultaBaseIirgd:

    @staticmethod
    async def serv_consulta_base_iirgd(param, service) -> dict:
        """
        nome: serv_consulta_base_iirgd
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        return_: dict = {}

        try:
            print(service)
            url_ = service.get("url") + "/Lista_Civil_CNH"

            headers_ = {
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
            return_ = await fetchPOST(url_, param, headers_)
            print("Retorno da API:", return_)

        except HTTPError as e:
            print(e.read())
            
            return_ = {}

        return return_
