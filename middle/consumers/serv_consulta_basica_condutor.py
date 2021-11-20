from api.utilities import fetchGET


class ServiceConsultaBasicaCondutor:

    @staticmethod
    async def serv_consulta_basica_condutor(request) -> dict:
        """
        nome: serv_consulta_basica_condutor
        :return: dict
        """

        url_: str
        headers_: dict
        params_: dict

        try:

            url_ = request["service"].get("url") + "/condutor/" + request["service"].get("canal") + "/consulta/basica/foto/reside/sp/" + str(int(request["parameters"].get("cpf"))) + "/registro/" + str(int(request["parameters"].get("numRegistro")))

            headers_ = {
                "Authorization": "Bearer " + request["service"].get("token"),
                "Accept": "application/json"
            }

        except Exception as e:
              print("Dados da requisição não foram enviados para consulta do serviço", e)
              return {}

        response_ = await fetchGET(url_, headers_)

        return response_
