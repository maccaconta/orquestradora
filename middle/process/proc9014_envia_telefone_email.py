from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9014EnviaTelefoneEmail(Consumers):

    async def get_envia_telefone_email(request_) -> dict:
        """
         name: get_envia_telefone_email
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}
        dddcel: list = []
        try:
            dddcel = str(request_["parameters"].get("proc9014_celular_completo", ""))
            ddd = dddcel[:2]
            cel = dddcel[2:11]
            params_["celular"] = int(cel)
            params_["cpf"] =  str(request_["parameters"].get("cpf", ""))
            params_["dddCelular"] = int(ddd)
            params_["email"] =  str(request_["parameters"].get("proc9014_email", ""))
            params_["registro"] =  str(request_["parameters"].get("numero_registro", ""))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_envia_telefone_email(params_, request_["service"])

        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9014_", context_)
                
                try:
                    cod_ = int(context_tratado_['proc9014_codigoInterno'])
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

