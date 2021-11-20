from middle.consumers.consumers import Consumers


class Proc024BuscaEndereco(Consumers):

    @staticmethod
    def get_busca_endereco(request_) -> dict:
        """
        name: get_busca_endereco
        :param request_: request
        :return: dict
        """
        _context = Consumers.serv_busca_endereco(request_)

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
