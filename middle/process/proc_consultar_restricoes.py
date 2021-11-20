from middle.consumers.consumers import Consumers


class ProcConsultarMultasRestricoes(Consumers):

    @staticmethod
    def proc_multas_restricoes(request_) -> dict:
        """
        nome: proc_multas_restricoes
        :param request_: request
        :return: expression_list
        """
        return {
            "text": "multa_restricoes",
            "context": {
                "ranavan": "xxxxxxxx",
                "multa": {"multa1": "xxxxxxx"}
            }
        }
