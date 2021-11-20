from api.utilities import fetchGET


class ServiceDataAgendamentoPoupatempo:

    @staticmethod
    async def serv_data_agendamento_poupatempo(request) -> dict:
        """
        nome: serv_data_agendamento_poupatempo
        :return: dict
        """

        url_: str
        headers_: dict
        params_: str

        try:
            url_ = request["service"]["url"] +"/v1/datas/orgaos/" + \
                    str(request["parameters"]["idOrgao"]) + "/locais/"+ \
                    str(request["parameters"]["posto_id"]) + "/servicos/" + str(request["parameters"]["idServico"])

            headers_ = {
                "Authorization": "Bearer " + request["service"].get("token")

            }

            fetch_ = url_

            response_ = await fetchGET(fetch_, headers_)

        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)
            return {}

        return response_
