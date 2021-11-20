from middle.consumers.consumers import Consumers


class Proc9044ConsultaBasicaCondutor(Consumers):

    async def get_consulta_basica_condutor(request_) -> dict:
        """
         name: get_consulta_basica_condutor
        :param request_: request
        :return: dict
        """

        return_: dict = {}

        _context = await Consumers.serv_consulta_basica_condutor(request_)

        if _context == {} or not _context:
            return_ = {
                "text": "api_nok",
                "context": {}
            }
        elif _context['codigoInterno'] != '0000':
            return_ = {
                "text": "api_erro",
                "context": {}
            }
        else:
            return_ = {
                "text": "api_ok",
                "context": _context
            }

        return_["context"]["process"] = ""

        return return_