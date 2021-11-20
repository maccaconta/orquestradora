from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc0006CepPoupatempo(Consumers):

    async def get_cep_poupatempo(request_) -> dict:
        """
         name: get_cep_poupatempo
        :param request_: request
        :return: dict
        """

        context_tratado_: dict = {}
        return_: dict = {}

        _context = await Consumers.serv_cep_poupatempo (request_)
        if _context == {} or not _context:
            return_ = {
                "text": "api_nok",
                "context": {}
            }
        else:
            if str(request_["parameters"]["proc0002_Cep"]) == "":
                return_ = {
                    "text": "api_erro",
                    "context": {
                        "msg": "Campo de CEP vazio.",
                        "process": ""
                    }
                }
            elif int(_context[0]["cdTipoCEP"]) != 1 and int(_context[0]["cdTipoCEP"]) != 2:
                
                return_ = {
                    "text": "api_erro",
                    "context": {
                        "msg": "Campo de CEP inválido.",
                        "process": ""
                    }
                }
            else:
                context_tratado_ = splitDict("proc0006_", _context[0])
                return_ = {
                    "text": "api_ok",
                    "context": context_tratado_
                }
               
        return_["context"]["process"] = ""
        return return_