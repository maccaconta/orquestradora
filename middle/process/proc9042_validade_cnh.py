from api.utilities import expiryValidation
from middle.consumers.consumers import Consumers


class Proc9042ValidadeCnh(Consumers):

    async def get_validade_cnh(request_) -> dict:
        """
        name: get_validade_cnh
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            # TODO: verificar parametros da requisição
            params_["cpf"] = str(request_["parameters"].get("cpf", ""))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC:", e)

        context_ = await Consumers.serv_validade_cnh(params_, request_["service"])

        if context_ == {} or context_ == None:
            return {
                "text": "api_nok",
                "context": {}
            } 
        else:
                
            try:
                # TODO: arrumar nomes dos campos passados na função
                valida_cnh_definitiva = expiryValidation(context_['validade_cnh'], context_['data_primeira_habilitacao'])
                context_tratado_ = context_
                context_tratado_['valida_cnh_definitiva'] = valida_cnh_definitiva['expired']
                context_tratado_['process'] = ''

                # TODO: verificar campos da resposta e arrumar condicionais do tratamento
                if 'codigoInterno' in context_tratado_:
                    return_ = {
                        'text': 'api_ok',
                        'context': context_tratado_
                    }

                elif 'codigo' in context_tratado_:
                    context_tratado_ = {
                        'text': 'api_erro',
                        'context': context_tratado_
                    }

                else:
                    return_ = {
                        'text': 'api_nok',
                        'context': {}
                    }

            except Exception as e:
                print("Falha na extração do codigo", e)
                return_ = {
                    'text': 'api_nok',
                    'context': {}
                }

        return return_

