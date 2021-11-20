from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9030CadastroEnderecoRecebimento(Consumers):

    @staticmethod
    async def get_cadastro_endereco_recebimento(request_) -> dict:
        """
        name: get_cadastro_endereco_recebimento
        :param request_: request
        :return: dict
        """
        params_: dict = {"cpf":"",
                         "enderecoRecebimento": {
                             "logradouro": "",
                             "numero": "",
                             "complemento": "",
                             "bairro": "",
                             "cep": "",
                             "codigoMunicipio": "",
                             "nomeMunicipio": ""
                             }
                         }

        retorno_: dict = {}

        params_["cpf"] = str(request_["parameters"].get("cpf", " "))
        params_["enderecoRecebimento"]["logradouro"] = str(request_["parameters"].get("proc9030_logradouro", " "))
        params_["enderecoRecebimento"]["numero"] = str(request_["parameters"].get("proc9030_numero", " "))
        params_["enderecoRecebimento"]["complemento"] = str(request_["parameters"].get("proc9030_complemento", " "))
        params_["enderecoRecebimento"]["bairro"] = str(request_["parameters"].get("proc9030_bairro", " "))
        params_["enderecoRecebimento"]["cep"] = str(request_["parameters"].get("proc9030_cep", " "))
        params_["enderecoRecebimento"]["codigoMunicipio"] = str(request_["parameters"].get("proc9030_codigoMunicipio", " "))
        params_["enderecoRecebimento"]["nomeMunicipio"] = str(request_["parameters"].get("proc9030_nomeMunicipio", " "))

        context_ = await Consumers.serv_cadastro_entrega_recebido(params_, request_["service"])

        if context_ == {}:
            retorno_ = {
                'text': 'api_nok',
                'context': {}
            }

        else:

            try:
                context_['mensagem'] = context_['mensagem'].lower()
            except:
                pass

            try:

                if int(context_['codigo']) == 0:

                    retorno_ = {
                        'text': 'api_ok',
                        'context': splitDict("proc9030_", context_)
                    }

                else:

                    # logradouro informado é inválido
                    # ------------------------------

                    if int(context_['codigo']) == 1101:

                        retorno_ = {
                            'text': 'api_erro',
                            'context': splitDict("proc9030_", context_)
                        }

                        context_["proc9030_logradouro"] = ""
                        context_["proc9030_bairro"] = ""
                        context_["proc9030_cep"] = ""
                        context_["proc9030_municipio"] = ""

                    else:

                        retorno_ = {
                            'text': 'api_erro',
                            'context': splitDict("proc9030_", context_)
                        }

            except:

                retorno_ = {
                    'text': 'api_nok',
                    'context': {}
                }

            retorno_["context"]["process"] = ""

            return retorno_