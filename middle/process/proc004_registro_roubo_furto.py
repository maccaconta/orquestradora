from middle.consumers.consumers import Consumers

class Proc004RegistroRouboFurto(Consumers):

    @staticmethod
    def get_registro_roubo_furto(request_) -> dict:
        """
        name: get_restricoes_debito
        :param request_: request
        :return: dict
        """
        _context = Consumers.serv_registro_roubo_furto(request_)

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
