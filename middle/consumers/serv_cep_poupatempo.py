from api.utilities import fetchGET


class ServiceCepPoupatempo:

    @staticmethod
    async def serv_cep_poupatempo(request) -> dict:
        """
        nome: serv_cep_poupatempo
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

            # params_ = str("06708480")
            params_ = str(request["parameters"].get("proc0002_Cep"))

            fetch_ = url_ + params_

        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)
            return {}

        response_ = await fetchGET(fetch_, headers_)

        return response_


