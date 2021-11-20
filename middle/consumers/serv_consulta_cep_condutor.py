from api.utilities import fetchGET


class ServiceConsultaCepCondutor:

    @staticmethod
    async def serv_consulta_cep_condutor(request) -> dict:
        """
        nome: serv_consulta_cep_condutor
        :return: dict
        """

        url_: str
        headers_: dict
        params_: dict

        try:

            url_ = request["service"].get("url") + "/consultaComMunicipioeBairro/"

            headers_ = {
                "Accept": "*/*",
                "Accept-Encodig": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            params_ = str(request["parameters"].get("cep"))

            fetch_ = url_ + params_

        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)
            return {}

        response_ = await fetchGET(fetch_, headers_)

        return response_
