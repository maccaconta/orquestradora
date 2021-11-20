from middle.consumers.consumers import Consumers


class Proc033RetornoSuspensao(Consumers):

    @staticmethod
    def get_retorno_suspensao(request_) -> dict:
        """
        name: get_retorno_suspensao
        :param request_: request
        :return: dict
        """
        _context = Consumers.serv_retorno_suspensao(request_)

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
