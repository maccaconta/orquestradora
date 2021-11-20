from api.utilities import splitDict
from middle.consumers.consumers import Consumers

class Proc9002ConsultarPontos(Consumers):
    async def get_consultar_pontos(request_) -> dict:
        """
         name: get_consultar_pontos
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}
        try:

            params_["periodo"] = str(request_["parameters"].get("periodo", " "))
            str(request_["parameters"].get("dataNascimento", " ")).replace('/','-')
            params_["tipo"] = int(request_["parameters"].get("tipo", " "))
            params_["numeroCnh"] = str(request_["parameters"].get("numeroCnh", " "))
            params_["dataNascimento"] = str(request_["parameters"].get("dataNascimento", " ")).replace('/','-')
            params_["cpf"] = str(request_["parameters"].get("cpf", " "))

        
        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)
        
        context_ = await Consumers.serv_consultar_pontos(params_, request_["service"])

        if context_ == {}:
            return {
                "text": "api_nok",
                "context":{}
            }
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9002_", context_)
                try:
                    cod_ = int(context_tratado_['proc9002_codigo'])
                    if cod_ == 0:
                        return_= {
                            'text': 'api_ok',
                            'context': context_tratado_
                        }
                    else:
                        return_ = {
                            'text': 'api_nok',
                            'context':""
                        }
                except Exception as e:
                    print("Falha na extração do codigo", e)
                    context_tratado_= "proc9002"
            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }
        return return_