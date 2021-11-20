from api.utilities import fetchPOST


class ServicePreCadatroPrimeiraHabilitacao:

    @staticmethod
    async def servSetPreCadatroPrimeiraHabilitacao(param, service) -> dict:
        """
        nome: Serviço para enviar o cadastro da primeira habilitação
                método POST
        :return: dict
        """

        url_: str = ""
        header_: dict = {}

        try:
            if service.get("token") == "" or \
                    service.get("url") == "" or \
                    service.get("canal") == "":
                print("Dados da requisção não foram enviados para consulta do serviço")
                return {}
        except:
            print("Dados da requisição não foram enviados para consulta do serviço")
            return {}

        url_ = service.get("url") + "/primeira-habilitacao/" + \
               service.get("canal") + "/gerar-pre-cadastro/"

        headers_ = {
            'Authorization': "Bearer " + service.get("token"),
            'Cache-Control': "no-cache",
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Connection': "keep-alive"
        }

        print("Parâmetros da requisição:", param )
        print(url_)

        try:
            retorno_ = await fetchPOST(url_, param, headers_)
            print("Retorno da API:", retorno_)

        except:
            retorno_ = {}

        return retorno_
