from api.utilities import fetchPOST, fetchVanzolini


class ServiceEndpointVanzolini:

    @staticmethod
    async def send_endpoint_vanzolini(param) -> dict:
        """
        nome: serv_buscar_horario_agendamento_psicologico
        :return: ...
        """
        url_: str = ""
        header_: dict = {}
        retorno: dict = {}

        url_ = "http://20.55.43.125/criaChamado"

        headers_ = {'Content-Type': 'application/json'}

        print("Parâmetros da requisição:", param)

        try:
            retorno_ = await fetchVanzolini(url_, param, headers_)
            print("Retorno da API:", retorno_)

        except:
            print("Retorno da API:", "sem retorno")

            retorno_ = {}

        return retorno_
