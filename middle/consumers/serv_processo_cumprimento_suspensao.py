

class ServiceProcessoComprimentoSuspensao:

    @staticmethod
    def serv_processo_cumprimento_suspensao(request) -> dict:
        """
        nome: serv_processo_cumprimento_suspensao
        :return: ...
        """

         # if (request["context"]["cpf"]):

        json_ = {
        "cumprimento": {
            "penalidade_cumprimento": "string",
            "data_inicio_cumprimento": "string"
            }
        }


        return json_
