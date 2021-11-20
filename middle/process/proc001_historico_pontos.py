from middle.consumers.consumers import Consumers
from api.models import Routers


class Proc001HistoricoPontos(Consumers):

    @staticmethod
    def get_historico_pontos(request_) -> dict:
        """
         name: get_historico_pontos
        :param request_: request
        :return: dict
        """
            
        _context = Consumers.serv_historico_pontos(request_)

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

            