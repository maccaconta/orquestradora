from api.utilities import fetchGET


class ServiceConsultaExameToxicologico:

    @staticmethod
    async def servConsultaExameToxicologico(request) -> dict:
        """
        nome: Serviço de consulta de exames toxicologicos Método GET
        :return: dict
        """

        url_: str
        headers_: dict
        params_: str

        try:
            url_ = request["service"].get("url") + "/cidadao/" + request["service"].get("canal") + "/consulta/exame/toxicologico/"

            headers_ = {
                "Authorization": "Bearer " + request["service"].get("token")
            }
            params_ = str(request["parameters"].get("cpf"))
            fetch_ = url_ + params_

        except Exception as e:
              print("Dados da requisição não foram enviados para consulta do serviço", e)
              return {}

        response_ = await fetchGET(fetch_, headers_)

        return response_
