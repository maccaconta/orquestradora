from api.utilities import fetchGET


class ServiceHorarioAgendamentoPoupatempo:

    @staticmethod
    async def serv_horario_agendamento_poupatempo(request) -> dict:
        """
        nome: serv_horario_agendamento_poupatempo
        :return: dict
        """
        url_: str
        headers_: dict
        data_: str

        data_ = request["parameters"]["data"][6:] + request["parameters"]["data"][3:5] + request["parameters"]["data"][:2]
        print(data_)
        try:
            url_ = request["service"]["url"] + "/v1/datas/horarios/orgaos/" + str(request["parameters"]["idOrgao"]) \
                + "/locais/"+ str(request["parameters"]["posto_id"]) +"/servicos/"\
                + str(request["parameters"]["idServico"]) + "/datas/" + data_

            # url_ = request["service"].get("url") + "/v1/datas/horarios/orgaos/" + request["parameters"].get("idOrgao", "") \
            #     + "/locais/" + request["parameters"].get("id1", "") + "/servicos/"\
            #     + request["parameters"].get("idServico", "") + "/datas/" + request["parameters"].get("data", "")

            headers_ = {
                "Authorization": "Bearer " + request["service"].get("token")
            }
                      
        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)
  
        response_ = await fetchGET(url_, headers_)

        return response_
