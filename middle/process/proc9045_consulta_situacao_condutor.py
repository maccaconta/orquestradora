from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9045ConsultaSituacaoCondutor(Consumers):

    async def get_consulta_situacao_condutor(request_) -> dict:
        """
         name: get_consulta_situacao_condutor
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            
            params_["cpf"] =  str(request_["parameters"].get("cpf", ""))
            params_["numero_registro"] =  str(request_["parameters"].get("numRegistro", ""))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_consulta_situacao_condutor(params_, request_["service"])

        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9045_", context_)
                
                try:
                    cod_ = int(context_tratado_['proc9045_codigo'])
                    if cod_ == 0:
                        return_ = {
                            'text': 'api_ok',
                            'context': context_tratado_
                        }

                    elif cod_ != '':
                        return_ = {
                            'text': 'api_erro',
                            'mensagem': context_tratado_["proc9045_mensagem"],
                            'context': context_tratado_
                            }
                    else:
                        return_ = {
                            'text': 'api_nok',
                            'context': context_
                }                       

                except Exception as e:
                    print("Falha na extração do codigo", e)
                    context_tratado_ = {}

            except Exception as e:
                print("Falha na criação do context tratado", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_
                }

        return_["context"]["process"] = ""

        return return_

