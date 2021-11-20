from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9046ConsultaBaseIirgd(Consumers):

    async def get_consulta_base_iirgd(request_) -> dict:
        """
         name: get_consulta_base_iirgd
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:

            tamanho = len(str(request_["parameters"].get("proc9028_numero_documento", ""))) - 1
        #05/08/2003
            data = str(request_["parameters"].get("data_expedicao", ""))
            dia = data[0:2]
            mes = data[3:5]
            ano = data[6:]
            data = ano + '-'+ mes + '-' + dia
        #2003-08-05

            params_["DATA_EXP"] =  data
            params_["MessageClassName"] =  'Lista_Civil_CNH'
            params_["RG"] = str(request_["parameters"].get("proc9028_numero_documento", ""))[0:tamanho]
            params_["RG_DIG"] =  str(request_["parameters"].get("proc9028_numero_documento", ""))[tamanho:]

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)
            
        context_ = await Consumers.serv_consulta_base_iirgd(params_, request_["service"])

        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9046_", context_)
                
                try:
                    cod_ = int(context_tratado_['proc9046_COD'])
                    if cod_ == 0:
                        return_ = {
                            'text': 'api_ok',
                            'context': context_tratado_
                        }

                    else:
                        return_ = {
                            'text': 'api_nok',
                            'context': {}
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

