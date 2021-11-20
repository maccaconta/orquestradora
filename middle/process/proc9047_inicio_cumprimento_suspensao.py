from api.utilities import splitDict
from middle.consumers.consumers import Consumers
from middle.utils.utils import assembly


class Proc9047InicioCumprimentoSuspensao(Consumers):

    async def get_inicio_cumprimento_suspensao(request_) -> dict:
        """
         name: get_consulta_rebaixamento
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        # print(request_["parameters"])
        try:
            params_["registro"] = str(request_["parameters"].get("numero_registro", " ")) 
            params_["cpf"] = str(request_["parameters"].get("cpf", " "))
            params_["penalidade_cumprimento"] = str(request_["parameters"].get("penalidade_cumprimento", " ")) 
            params_["data_inicio_cumprimento"] = str(request_["parameters"].get("data_inicio_cumprimento", " ")) 
            params_["data_fim_cumprimento"] = str(request_["parameters"].get("data_fim_cumprimento", " "))
            params_["portarias"] = request_["parameters"].get("portarias", " ")

            for data in params_["portarias"]:
                assembly(data)

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_inicio_cumprimento_suspensao(params_, request_["service"])

        print(f'CONTEXT ---> {context_}')

        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9047_", context_)
                return_ = {
                    'text': 'api_ok',
                    'context': context_tratado_
                    }

                # for c in range(0, len(context_tratado_["proc9047_inicioCumprimentoSuspensao"])):
                #     context_tratado_["proc9047_inicioCumprimentoSuspensao" + str(c)] = context_tratado_["proc9047_inicioCumprimentoSuspensao"][c]
                # try:
                #     if context_tratado_['proc9047_codigo'] is True:
                #         cod_ = context_tratado_['proc9047_codigo']
                #     elif context_tratado_['proc9047_codigoInterno'] is True:
                #         cod_ = context_tratado_['proc9047_codigoInterno']
                #     if cod_ == 0:
                #         return_ = {
                #             'text': 'api_ok',
                #             'context': context_tratado_
                #         }

                #     else:

                # except Exception as e:
                #     print("Falha na extração do codigo", e)
                #     context_tratado_ = "proc9047"

            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }
        return_["context"]["process"] = ""
        return return_

