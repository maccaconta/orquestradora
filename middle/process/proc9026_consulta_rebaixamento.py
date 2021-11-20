from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9026ConsultaRebaixamento(Consumers):

    async def get_consulta_rebaixamento(request_) -> dict:
        """
         name: get_consulta_rebaixamento
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            params_["cpfCondutor"] =  str(request_["parameters"].get("cpf", " "))
        
        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)
        context_ = await Consumers.serv_consulta_rebaixamento(params_, request_["service"])

        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9026_", context_)

                # for c in range(0, len(context_tratado_["proc9026_categoriaOpcaoRebaixamento"])):
                #     context_tratado_["proc9026_categoriaOpcaoRebaixamento" + str(c)] = context_tratado_["proc9026_categoriaOpcaoRebaixamento"][c]
                try: 
                    if 'proc9026_codigo' in context_tratado_:
                        cod_ = context_tratado_['proc9026_codigo'].lower()
                    elif 'proc9026_codigoInterno' in context_tratado_:
                        cod_ = context_tratado_['proc9026_codigoInterno'].lower()
                    if cod_ == 1:
                        context_tratado_["proc9026_mensagem"] = cod_
                        return_ = {
                            "text": "api_erro",
                            "context": context_tratado_
                        }                       

                    elif int(cod_) == 0 or int(cod_) == 7:
                        return_ = {
                            "text": "api_ok",
                            "context": context_tratado_
                        }
                    elif cod_ == 1500:

                        return_ = {
                            'text': 'api_nok',
                            'context': context_tratado_
                        }

                    elif cod_ == 204 or cod_ == 1:

                        return_ = {
                            'text': 'api_erro',
                            'context': context_tratado_
                        }

                except Exception as e:
                    print("Erro no tratamento do retorno:", e)

                    return_ = {
                        'text': 'api_nok',
                        'context': context_tratado_
                    }

            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }
                
        return_["context"]["process"] = ""
        return return_

