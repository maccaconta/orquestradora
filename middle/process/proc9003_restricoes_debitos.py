from api.utilities import splitDict
from middle.consumers.consumers import Consumers

class Proc9003RestricoesDebitos(Consumers):
    async def get_restricoes_debitos(request_) -> dict:
        """
         name: get_consulta_rebaixamento
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}
        try:
            
            params_["cpf"] = str(request_["parameters"].get("cpf", " "))
            params_["placa"] = str(request_["parameters"].get("placa", " "))
            params_["renavam"] = str(request_["parameters"].get("renavam", " "))

        
        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)
        
        context_ = await Consumers.serv_restricoes_debitos(params_, request_["service"])

        if context_ == {}:
            return {
                "text": "api_nok",
                "context":{}
            }
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9003_", context_)
                try:
                    cod_ = int(context_tratado_['proc9003_codigo'])
                    if cod_ == 0:
                        return_= {
                            'text': 'api_ok',
                            'context': context_tratado_
                        }
                    elif cod_ == 317 or cod_ == 4:
                         return_= {
                            'text': 'api_erro',
                            'context': context_tratado_
                        }                       
                    else:
                        return_ = {
                            'text': 'api_nok',
                            'context':""
                        }
                except Exception as e:
                    print("Falha na extração do codigo", e)
                    context_tratado_= "proc9003"
            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }
        return return_