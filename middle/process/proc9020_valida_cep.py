from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9020ValidaCep(Consumers):

    async def get_valida_cep(request_) -> dict:
        """
         name: get_consulta_rebaixamento
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            params_["cep"] =  str(request_["parameters"].get("cep", " "))
            params_["cpf_cnpj"] =  str(request_["parameters"].get("cpf_cnpj", " "))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_valida_cep(params_, request_["service"])

        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9020_", context_)
                
                try:
                    cod_ = int(context_tratado_['proc9020_codigo'])
                    if cod_ == 0:
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
                    context_tratado_ = "proc9020"

            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }

        return return_

