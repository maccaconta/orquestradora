from middle.consumers.consumers import Consumers


class Proc9048ConsultaCepCondutor(Consumers):

    async def get_consulta_cep_condutor(request_) -> dict:
        """
         name: get_consulta_cep_condutor
        :param request_: request
        :return: dict
        """

        return_: dict = {}

        _context = await Consumers.serv_consulta_cep_condutor(request_)

        if _context == {} or not _context:
            return_ = {
                "text": "api_nok",
                "context": {}
            }
        else:
            context_: dict = {}

            context_["proc9030_codigoMunicipio"] = str(_context[0]["numeroIBGE"])
            context_["proc9030_nomeMunicipio"] = _context[0]["municipio"]

            return_ = {
                "text": "api_ok",
                "context": context_
            }

        context_["process"] = ""

        return return_
