from middle.consumers.consumers import Consumers
from middle.utils.utils import assembly


class Proc9035EnviarToken(Consumers):

    async def get_enviar_token(request_) -> dict:
        """
         name: get_consulta_rebaixamento
        :param request_: request
        :return: dict
        """
        
        params_: dict = {}
        context_: dict = {}
        return_: dict = {}
        DDDtelefone: list = []
        try:
            DDDtelefone = str(request_["parameters"].get("proc9035_celular", ""))
            telDDD = DDDtelefone[:2]
            telcelular = DDDtelefone[2:]
            params_["prefixo"] = str(request_["parameters"].get("prefixo", ""))
            params_["cpf"] = str(request_["parameters"].get("cpf", ""))
            params_["nome"] = str(request_["parameters"].get("nome", ""))
            params_["email"] = str(request_["parameters"].get("email", ""))
            params_["telefoneDdd"] = str(telDDD)
            params_["telefoneNumero"] = str(telcelular)
            params_["mensagem"] = str(request_["parameters"].get("watson_mensagem", ""))
    
            assembly(params_)
            
        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_enviar_token(params_, request_["service"])
        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            } 
                      
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = {"response": context_}
                
                try:
                    if context_tratado_['response'] == True:
                        context_tratado_["telefone"]=  f' ({params_["telefoneDdd"]}){params_["telefoneNumero"]} '
                        return_ = {
                            'text': 'api_ok',
                            'context': context_tratado_
                        }

                    else:
                        return_ = {
                            'text': 'api_nok',
                            'context': ""
                            }

                except Exception as e:
                    print("Falha na extração do codigo", e)
                    context_tratado_ = "proc9035"

            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }

        return return_

