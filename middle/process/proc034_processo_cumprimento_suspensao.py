from middle.consumers.consumers import Consumers


class Proc034ProcessoCumprimentoSuspensao(Consumers):

    @staticmethod
    def get_processo_cumprimento_suspensao(request_) -> dict:
        """
        name: get_processo_cumprimento_suspensao
        :param request_: request
        :return: dict
        """
        _context = Consumers.serv_processo_cumprimento_suspensao(request_)

        if _context == {}:
            return {
                "text": "api_nok",
                "context": {}
            }
        else:

            return {
                "text": "api_ok",
                "context": _context
            }
