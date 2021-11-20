from middle.consumers.consumers import Consumers


class ProcValidarCadastro(Consumers):

    @staticmethod
    def proc_validar_cadastro(request_) -> dict:
        """
         name: proc_validar_cadastro
        :param request_: request
        :return: expression_list
        """
        _context = Consumers.serv_cadastro_cidadao(request_)

        return {
            "text": "cadastro_valido",
            "context": _context
        }
