from api.utilities import splitDict
from middle.consumers.consumers import Consumers

class Proc9052ConsultarSegundaVia(Consumers):
    async def get_consultar_segunda_via(request_) -> dict:
        """
         name: get_consultar_segunda_via
        :param request_: request
        :return: dict
        """
        return_: dict = {}
        
        context_ = await Consumers.serv_consultar_segunda_via(request_)

        if context_ == {} or not context_:
                    return_ = {
                        "text": "api_nok",
                        "context": {}
                    }
        elif context_['codigoInterno'] != '0000':
            return_ = {
                "text": "api_erro",
                "context": {}
            }
        else:
            return_ = {
                "text": "api_ok",
                "context": context_
            }

        return_["context"]["process"] = ""

        return return_