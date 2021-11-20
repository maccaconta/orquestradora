from middle.consumers.consumers import Consumers

class proc9016_endpoint_vanzolini(Consumers):
    from api.utilities import splitDict
    from middle.consumers.consumers import Consumers

    @staticmethod
    async def proc_endpoint_vanzolini(request_) -> dict:
        """
        name: get_cadastro_endereco_recebimento
        :param request_: request
        :return: dict
        """

        params_: dict = {
            'secret': "",
            'pergunta': "",
            'categoria_id': "",
            'nome': "",
            'watson_node_id': "",
            'dados_adicionais': {
                'campo': ""
            }
        }

        context_: str = ""

        try:

            if "CNH" in request_["parameters"].get("categoria_id", ""):
                categoria_id = 1
            elif "Veículo" in request_["parameters"].get("categoria_id", ""):
                categoria_id = 2
            elif "Infração" in request_["parameters"].get("categoria_id", ""):
                categoria_id = 3
            else:
                categoria_id = 1

            params_['secret'] = "CHAVE-API-KG83HTY7DK340GJ476J39FKJ05MF63H"
            params_['categoria_id'] = categoria_id
            params_['pergunta'] = str(request_["parameters"].get("user_input", ""))
            params_['nome'] = str(request_["parameters"].get("nome_saudacao", ""))
            params_['watson_node_id'] = ""
            params_['dados_adicionais']['campo'] = str(request_["parameters"].get("email", ""))

            context_ = await Consumers.send_endpoint_vanzolini(params_)

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        if "sucesso" in context_:

            retorno_ = {
                'text': 'api_ok',
                'context': {}
            }

        else:

            retorno_ = {
                'text': 'api_nok',
                'context': {}
            }

        retorno_["context"]["process"] = ""
        retorno_["context"]["user_input"] = ""

        return retorno_
