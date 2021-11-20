from api.utilities import fetchPOST


class ServiceSolicitarSegundaViaCnh:

    @staticmethod
    async def serv_solicitar_segunda_via_cnh(param, service) -> dict:
        """
        nome: serv_solicitar_segunda_via_cnh
        :return: ...
        """

        url_: str = ""
        header_: dict = {}
        retorno: dict = {}


        url_ = service.get("url") + "/rest/" + \
               "/segundaViaCnh/" + "/solicita/"

        headers_ = {
            'Authorization': "Bearer " + service.get("token"),
            'Cache-Control': "no-cache",
            'Content-Type': "application/json; charset=UTF-8",
            'Accept': "*/*",
            'Connection': "keep-alive"
        }

        print("Parâmetros da requisição:", param)

        try:
            retorno_ = await fetchPOST(url_, param, headers_)
            print("Retorno da API:", retorno_)

        except Exception as e:
            print("Retorno da API:", e)

            retorno_ = {}

        return retorno_
