from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9027AgendamentoMedicoCapitalMicroRegiao(Consumers):

    @staticmethod
    async def get_agendamento_medico_capital_micro_regiao(request_) -> dict:
        """
        name: get_cadastro_endereco_recebimento
        :param request_: request
        :return: dict
        """
        params_: dict = {}
        retorno_: dict = {}
        context_: dict = {}

        try:
            params_["cpf_cidadao"] = str(request_["parameters"].get("cpf", ""))
            params_["tipo_exame"] = str(request_["parameters"].get("tipo_exame", "MEDICO"))
            params_["usuario"] = request_["service"].get("canal").upper()

            params_["is_portador_necessidades_especiais"] = True \
                if str(request_["parameters"].get("is_portador_necessidades_especiais", "SIM")).upper() == "SIM" \
                else False

            # params_["cep_cidadao"] = request_["parameters"].get("proc9007_cep")
            params_["id_regiao_medico"] = request_["parameters"].get("proc9008_regioes_medico_long_id", 1)
            params_["id_regiao_psicologo"] = request_["parameters"].get("id_regiao_psicologo", 0)

            context_ = await Consumers.servAgendamentoMedicoCapitalMicroRegiao(params_, request_["service"])
            context_tratado_ = splitDict("proc9027_", context_)
        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        if context_ == {}:

            retorno_ = {
                'text': 'api_nok',
                'context': {}
            }

        else:
            cod_ = int(context_.get("codigo", 0))

            if cod_ == 400:
                retorno_ = {
                    'text': 'api_erro',
                    'context': {
                        "codigo": context_['codigo'],
                        "mensagem": context_['mensagem']
                    }
                }

            else:
                retorno_ = {
                    'text': 'api_ok',
                    'context': context_tratado_
                }

        retorno_["context"]["process"] = ""

        return retorno_
