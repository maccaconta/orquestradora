from api.utilities import fetchPOST


class ServiceRealizarAgendamentoMedicoRenovacao:

    @staticmethod
    async def serviceRealizarAgendamentoMedicoRenovacao(param, service) -> dict:
        """
        nome: serv_realizar_agendamento_medico_renovacao
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

        url_ = service.get("url") + "/divisao-equitativa/" + \
               service.get("canal") + "/agendar-exame-medico/"

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
