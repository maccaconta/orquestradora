from api.utilities import fetchPOST


class ServiceSolicitaCnhDefinitiva:

    @staticmethod
    async def serv_solicita_cnh_definitiva(param, service) -> dict:
        """
        nome: serv_solicita_cnh_definitiva
        :return: ...
        """

        url_: str = ""
        headers_: dict = {}
        return_: dict = {}

        try:
            if service.get("token") == "" or \
                    service.get("url") == "" or \
                    service.get("canal") == "":
                print("Dados da requisção não foram enviados para consulta do serviço")
                return {}
        except:
            print("Dados da requisição não foram enviados para consulta do serviço")
            return {}

        # TODO: verificar url
        url_ = service.get("url") + "/renach/" + \
               service.get("canal") + "/gerar-2-via/"

        headers_ = {
            'Authorization': "Bearer " + service.get("token"),
            'Cache-Control': "no-cache",
            'Content-Type': "application/json; charset=UTF-8",
            'Accept': "*/*",
            'Connection': "keep-alive"
        }

        print("Parâmetros da requisição:", param)

        try:
            return_ = await fetchPOST(url_, param, headers_)
            print("Retorno da API:", return_)

        except Exception as e:
            print("Retorno da API:", e)

            return_ = {}

        return return_
