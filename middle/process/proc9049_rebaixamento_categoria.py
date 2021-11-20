from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9049RebaixamentoCategoria(Consumers):

    async def get_rebaixamento_categoria(request_) -> dict:
        """
         name: get_consulta_rebaixamento
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            params_["categoriaRebaixamento"] =  str(request_["parameters"].get("categoriaRebaixamento", " "))
            params_["cpfCondutor"] =  str(request_["parameters"].get("cpf", " "))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_rebaixamento_categoria(params_, request_["service"])
        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9049_", context_)    
                try:
                    cod_ = int(context_tratado_['proc9049_codigoInterno'])
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
                    context_tratado_ = "proc9049"

            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }

        return return_

