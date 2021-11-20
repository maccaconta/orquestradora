from api.utilities import splitDict
from middle.consumers.consumers import Consumers
from middle.utils.utils import assembly


class proc9036ValidarToken(Consumers):

    async def get_validar_token(request_) -> dict:
        """
         name: get_validar_token
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            params_["prefixo"] = str(request_["parameters"].get("prefixo", " "))
            params_["cpf"] = str(request_["parameters"].get("cpf", " "))
            params_["token"] = str(request_["parameters"].get("token", " "))

            assembly(params_)
 
        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_validar_token(params_, request_["service"])
        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                # context_tratado_ = {"response": context_}
                # for c in range(0, len(context_tratado_["proc9036_validarToken"])):
                #     context_tratado_["proc9036_validarToken" + str(c)] = context_tratado_["proc9036_validarToken"][c]
                
                try:
                    if context_['status'] in [200, 201]:
                        return_ = {
                            'text': 'api_ok',
                            'context': {'message': 'success'}
                        }
                    else:
                        return_ = {
                            'text': 'api_nok',
                            'context': {'message': 'fail'}
                            }

                except Exception as e:
                    print("Falha na extração do codigo", e)
                    context_tratado_ = "proc9036"

            except Exception as e:
                print("Falha na atualização da matriz", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }
        
        return_["context"]["process"] = ""

        return return_


