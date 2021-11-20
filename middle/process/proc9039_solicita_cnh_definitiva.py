from middle.consumers.consumers import Consumers


class Proc9039SolicitaCnhDefinitiva(Consumers):

    async def get_solicita_cnh_definitiva(request_) -> dict:
        """
        name: get_solicita_cnh_definitiva
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

        context_ = await Consumers.serv_solicita_cnh_definitiva(params_, request_["service"])

        if context_ == {} or context_ == None:
            return {
                "text": "api_nok",
                "context": {}
            } 
        else:
                
            try:
                
                # TODO: verificar campos da resposta e arrumar condicionais do tratamento
                if 'codigoInterno' in context_:
                    return_ = {
                        'text': 'api_ok',
                        'context': context_
                    }

                elif 'codigo' in context_:
                    context_ = {
                        'text': 'api_erro',
                        'context': context_
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

