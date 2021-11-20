from middle.consumers.consumers import Consumers


class Proc9051ConsultaMunicipioPais(Consumers):

    def get_codigo_municio_pais(request_) -> dict:
        """
         name: get_codigo_municio_pais
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        
        try:
            params_["type"] = str(request_["parameters"].get("type", " "))
            params_["name"] = str(request_["parameters"].get("name", " "))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = Consumers.serv_consulta_codigo_cidade_pais(params_)

        if context_ == {}:
            return {
                    "text": "api_nok",
                    "context": {}
                    }            
        else:
            return {
                    "text": "api_ok",
                    "context": {
                        "naturalidade": context_
                    }
                    }