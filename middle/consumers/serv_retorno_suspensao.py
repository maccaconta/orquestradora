

class ServiceRetornoSuspensao:

    @staticmethod
    def serv_retorno_suspensao(request) -> dict:
        """
        nome: serv_retorno_suspensao
        :return: ...
        """

        # if (request["context"]["cpf"]):
        if (request["retorno_suspensao"]):

            json_ = {
            "cpf": "123456789",
            "nome": "Luciana",
            "registro_cnh": 0,
            "numero_processo": 0,
            "status_cnh": "ok",
            "pena": "bla",
            "cumprimento": {
                "penalidade_cumprimento": "string",
                "data_inicio_cumprimento": "string",
                "data_fim_cumprimento": "string"
                }
            }


        return json_
