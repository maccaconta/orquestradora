from api.utilities import fetchPOST
from urllib.error import HTTPError


class ServiceEnviaTelefoneEmail:

    @staticmethod
    async def serv_envia_telefone_email(param, service) -> dict:
        """
        nome: serv_envia_telefone_email
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        return_: dict = {}

        try:
            url_ = service.get("url") + "/cidadao/" + \
                service.get("canal") + "/registrar/contato/"

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
