from api.utilities import fetchGET


class ServiceConsultarSegundaVia:

    @staticmethod
    async def serv_consultar_segunda_via(request) -> dict:
        """
        nome: serv_consultar_validade_cnh
        :return: ...
        """

        url_: str = ""
        header_: dict = {}
        retorno: dict = {}

        try:
            url_ = request["service"].get("url") + "/rest/" + \
                "/segundaViaCnh/" + "/consulta/" + "/cpf/" + \
                 str(request["parameters"].get("cpf", " ")) +  "/registro/" + str(request["parameters"].get("registro", " "))

            headers_ = {
                "Authorization": "Bearer " + request["service"].get("token"),
                "Accept": "application/json"
            }

        except Exception as e:
              print("Dados da requisição não foram enviados para consulta do serviço", e)
              return {}

        response_ = await fetchGET(url_, headers_)

        return response_

  