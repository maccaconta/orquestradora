from middle.consumers.consumers import Consumers


class Proc025CadastroCepEndereco(Consumers):

    @staticmethod
    def get_cadastro_cep_endereco(request_) -> dict:
        """
        name: get_cadastro_cep_endereco
        :param request_: request
        :return: dict
        """
        _context = Consumers.serv_cadastro_cep_endereco(request_)

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
