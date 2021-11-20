import datetime

from api.utilities import fetchPOST


class ServiceCadastroEnderecoRecebido:

    @staticmethod
    async def serv_cadastro_entrega_recebido(param, service) -> dict:
        """
        nome: serv_cadastro_entrega_recebido
        :return: ...
        """

        try:
            if service.get("token") == "" or \
                    service.get("url") == "" or \
                    service.get("canal") == "":
                print("Dados da requisção não foram enviados para consulta do serviço")
                return {}
        except:
            print("Dados da requisição não foram enviados para consulta do serviço")
            return {}

        url_ = service.get("url") + "/condutor/" + \
               service.get("canal") + "/cadastro-enderecos"

        headers_ = {
            'Authorization': "Bearer " + service.get("token"),
            'Cache-Control': "no-cache",
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Connection': "keep-alive"
        }

        print("Parâmetros da requisição:", param)
        print("url", url_)

        try:
            retorno_ = await fetchPOST(url_, param, headers_)
            print("Retorno da API:", retorno_)

        except:
            retorno = {}

        return retorno_