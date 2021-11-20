from api.utilities import fetchPOST


class ServiceConsultaRG:

    @staticmethod
    async def servConsultaRG(param, service) -> dict:
        """
        nome: serv_buscar_horario_agendamento_psicologico
        :return: ...
        """
        url_: str = ""
        header_: dict = {}
        retorno: dict = {}

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
               service.get("canal") + "/consulta-rg/"

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

        except:
            print("Retorno da API:", "sem retorno")

            retorno_ = {}

        return retorno_
