from api.utilities import fetchPOST
from urllib.error import HTTPError


class ServiceConsultaSituacaoCondutor:

    @staticmethod
    async def serv_consulta_situacao_condutor(param, service) -> dict:
        """
        nome: serv_consulta_situacao_condutor
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        return_: dict = {}

        try:
            url_ = service.get("url") + "/condutor/" + \
                service.get("canal") + "/consulta-situacao/"

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
            return_ = await fetchPOST(url_, param, headers_)
            print("Retorno da API:", return_)

        except HTTPError as e:
            print(e.read())
            
            return_ = {}

        return return_
