from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9006EnderecoParaEntrega(Consumers):

    async def get_endereco_para_entrega(request) -> dict:
        """
        name: get_endereco_para_entrega
        :param request_: request
        :return: dict
        """

        context_: dict = {}
        retorno_: dict = {}

        params_ = {
            "cpf": str(request["parameters"].get("cpf", ""))
        }

        context_ = await Consumers.serv_endereco_para_entrega(params_, request["service"])

        context_['mensagem'] = context_['mensagem'].lower()

        try:
            context_["end_resumo"] = "1. Endereço do cadastro :" + \
                                    context_["enderecoCadastro"]["logradouro"].lower() + ", " + \
                                     context_["enderecoCadastro"]["numero"] + " - " + \
                                     context_["enderecoCadastro"]["complemento"] + " - bairro: " + \
                                     context_["enderecoCadastro"]["bairro"] + " -  cidade: " + \
                                     context_["enderecoCadastro"]["nomeMunicipio"] + " - cep: " + \
                                     context_["enderecoCadastro"]["cep"]

        except:
            context_["end_resumo"] = "cadastro"

        try:
            context_["end_recebe_2"] = "2. Endereço de Recebimento :" + \
                                       context_[0]["enderecosRecebimento"]["logradouro"].lower() + ", " + \
                                       context_[0]["enderecosRecebimento"]["numero"] + " - " + \
                                       context_[0]["enderecosRecebimento"]["complemento"] + " - bairro: " + \
                                       context_[0]["enderecosRecebimento"]["bairro"] + " -  cidade: " + \
                                       context_[0]["enderecosRecebimento"]["nomeMunicipio"] + " - cep: " + \
                                       context_[0]["enderecosRecebimento"]["cep"]


        except:
            context_["end_recebe_2"] = ""


        try:
            context_["end_recebe_3"] = "3. Endereço de Recebimento :" + \
                                       context_[1]["enderecosRecebimento"]["logradouro"].lower() + ", " + \
                                       context_[1]["enderecosRecebimento"]["numero"] + " - " + \
                                       context_[1]["enderecosRecebimento"]["complemento"] + " - bairro: " + \
                                       context_[1]["enderecosRecebimento"]["bairro"] + " -  cidade: " + \
                                       context_[1]["enderecosRecebimento"]["nomeMunicipio"] + " - cep: " + \
                                       context_[1]["enderecosRecebimento"]["cep"]
        except:
            context_["end_recebe_3"] = ""

        try:
            context_['mensagem'] = context_['mensagem'].lower()
        except:
            pass

        if context_ == {}:
            retorno_ = {
                "text": "api_nok",
                "context": {}
            }

        else:

            try:

                # todo: tratar CPF , {'codigo': 1500, 'mensagem': 'cpf informado(a) é inválido(a).'}

                if context_['mensagem'] == "consulta efetuada com sucesso":

                    context_tratado_: dict = {}

                    context_tratado_ = splitDict("proc9006_", context_)
                    context_tratado_["9006_Endereços_Cadastrados"] = str('3-Endereço de recebimento:' + context_["end_recebe_2"] + context_["end_recebe_3"])
                    retorno_ = {
                        'text': 'api_ok',
                        'context': context_tratado_
                    }

                else:
                    retorno_ = {
                        "text": "api_nok",
                        "context": {}
                    }

            except:
                retorno_ = {
                    "text": "api_nok",
                    "context": {}
                }

            retorno_["context"]["process"] = ""

            return retorno_