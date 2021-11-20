from middle.consumers.consumers import Consumers
from common.utils import Formatted


class Proc0007AcompanhamentoEmissaoRg(Consumers):

    async def get_acompanhamento_emissao_rg(request_) -> dict:
        """
         name: get_acompanhamento_emissao_rg
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        rg_: str = ""
        cpf_: str = ""

        try:

            rg_ = Formatted(str(request_["parameters"].get("numero_rg", "")))
            cpf_ = Formatted(str(request_["parameters"].get("numero_cpf", "")))

            params_["cpfDigito"] = str(cpf_[-2:])
            params_["cpfNumero"] = str(cpf_[:-2])
            params_["registroSequencia"] = ""
            params_["registroNumero"] = str(rg_[:-1])
            params_["registroDigito"] = str(rg_[-1:])

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_acompanhamento_emissao_rg(params_, request_["service"])

        if type(context_) is dict:
            if context_ == {} or not context_:
                return {
                    "text": "api_nok",
                    "context": {}

                }

        if 'code' in context_:
            cont_erros = int(request_["context"].get("cont_erros", 0))
            cont_erros += 1
            context_["cont_erros"] = cont_erros
            context_["process"] = ""
            return {
                'text': 'api_erro',
                'context': context_
            }

        if type(context_) is list:
            for item in context_:

                if 'Registro não encontrado' in item["Mensagem"]:
                    cont_erros = int(request_["context"].get("cont_erros", 0))
                    cont_erros += 1
                    return {
                        "text": "api_erro",
                        "context": {"proc0007_msg": "O CPF ou RG informado não foi encontrado no nosso cadastro",
                                    "cont_erros": cont_erros,
                                    "process": ""
                                    }
                    }

        else:
            context_["process"] = ""
            return {
                'text': 'api_ok',
                'context': context_
            }
