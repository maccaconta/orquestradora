# from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9040SolicitarSegundaViaCnh(Consumers):

    async def get_solicitar_segunda_via_cnh(request_) -> dict:
        """
        name: get_solicitar_segunda_via_cnh
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            params_["bairro"] = str(request_["parameters"].get("bairro", ""))
            params_["categoria"] = str(request_["parameters"].get("categoria", ""))
            params_["cep"] = str(request_["parameters"].get("cep", ""))
            params_["complemento"] = str(request_["parameters"].get("complemento", ""))
            params_["cpf"] = str(request_["parameters"].get("cpf", ""))
            params_["logradouro"] = str(request_["parameters"].get("logradouro", ""))
            params_["municipio"] = str(request_["parameters"].get("municipio", ""))
            params_["nome"] = str(request_["parameters"].get("nome", ""))
            params_["numero"] = str(request_["parameters"].get("numero", ""))
            params_["registro"] = str(request_["parameters"].get("registro", ""))
            params_["tipoServico"] = str(request_["parameters"].get("tipoServico", ""))
            params_["validadeCnh"] = str(request_["parameters"].get("validadeCnh", ""))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC:", e)

        context_ = await Consumers.serv_solicitar_segunda_via_cnh(params_, request_["service"])

        if context_ == {} or context_ == None:
            return {
                "text": "api_nok",
                "context": {}
            } 
        else:
                
            try:
                
                if 'codigoInterno' in context_:
                    return_ = {
                        'text': 'api_ok',
                        'context': context_
                    }

                elif 'codigo' in context_:
                    return_ = {
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

