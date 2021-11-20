from api.utilities import fetchPOST
from urllib.error import HTTPError
import json
from middle.utils.utils import search_url


class ServiceValidarToken:

    @staticmethod
    async def serv_validar_token(param, service) -> dict:
        """
        nome: serv_validar_token
        :return: ...
        """

        url_: str = ""
        header_: dict = {}
        retorno: dict = {}
        
        try:
            #url_ = service.get("url") + "/sms/" + \
                #service.get("canal") + "/valida-token"
            data = await search_url('sms')
            url_ = f'{data.url_serv_homo}/sms/{service["canal"]}/valida-token'
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
            print(f'ERROR: {url_}, {param}')
            retorno_ = await fetchPOST(url_, param, headers_)
        except HTTPError as e:
            
            
            retorno_ = {}

        return retorno_
        