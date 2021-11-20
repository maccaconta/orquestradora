from middle.consumers.consumers import Consumers


class Proc9007ExibirDadosPessoais(Consumers):

    @staticmethod
    async def get_exibir_dados_pessoais(request_) -> dict:
        """
        name: get_exibir_dados_pessoais
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        params_["cpf"] = str(request_["parameters"].get("cpf"))

        context_ = await Consumers.serv_exibir_dados_pessoais(params_, request_["service"])
        
        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }
        else:
            try:

                # context_["email"] = context_["email"]
                # context_["telefoneNumero"] = context_["celular"]
                # context_["telefoneDdd"] = context_["ddd_celular"]
                
                try:

                    cod_ = int(context_['codigo'])

                    if cod_ == 0 or cod_ == 7:
                        return_ = {
                            "text": "api_ok",
                            "context": context_
                        }
                    elif cod_ == 1500:

                        return_ = {
                            'text': 'api_nok',
                            'context': context_
                        }

                    elif cod_ == 204:

                        return_ = {
                            'text': 'api_erro',
                            'context': context_
                        }


                except Exception as e:
                    print("Erro no tratamento do retorno:", e)

                    return_ = {
                        'text': 'api_nok',
                        'context': context_
                    }

            except Exception as e:
                print("Erro nos ajustes do contexto:", e)

                return_ = {
                    'text': "api_nok",
                    'context': context_
                }
        return_["context"]["process"] = ""

        return return_
