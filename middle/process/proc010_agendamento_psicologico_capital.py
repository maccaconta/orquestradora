from middle.consumers.consumers import Consumers


class Proc010AgendamentoPsicologicoCapital(Consumers):

    @staticmethod
    def get_agendamento_psicologico_capital(request_) -> dict:
        """
        name: get_agendamento_psicologico_capital
        :param request_: request
        :return: dict
        """
        _context = Consumers.serv_agendamento_psicologico_capital(request_)

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