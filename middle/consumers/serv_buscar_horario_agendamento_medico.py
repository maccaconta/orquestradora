from api.utilities import fetchPOST


class ServiceBuscarHorarioAgendamentoMedico:

    @staticmethod
    async def serv_buscar_horario_agendamento_medico(param, service) -> dict:
        """
        nome: serv_agendamento_medico_capital
        :return: ...
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

        url_ = service.get("url") + "/divisao-equitativa/" + \
               service.get("canal") + "/horarios-por-data/"

        headers_ = {
            'Authorization': "Bearer " + service.get("token"),
            'Cache-Control': "no-cache",
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Connection': "keep-alive"
        }

        print("Parâmetros da requisição:", param)
        print(url_)

        try:
            retorno_ = await fetchPOST(url_, param, headers_)
            print("Retorno da API:", retorno_)

        except:
            retorno_ = {}

        return retorno_