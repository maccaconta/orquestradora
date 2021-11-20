from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9013RealizarAgendamentoMedicoPsicologico(Consumers):

    async def setRealizarAgendamentoMedicoPsicologico(request_) -> dict:
        """
        name: get_buscar_horario_agendamento_psicologico
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        retorno_: dict = {}
        context_: dict = {}
        data_: dict = {}

        try:

            params_["cpf_cidadao"] = request_["parameters"].get("cpf", 0)
            params_["tipo_processo"] = "PRIMEIRA_HABILITACAO"
            params_["cep_cidadao"] = int(request_["parameters"].get("cep"))
            params_["codigo_ciretran_exame_medico"] = int(request_["parameters"].get("codigo_ciretran", 0))
            params_["categoria_pretendida"] = int(request_["parameters"].get("categoria_pretendida", 0))
            params_["id_medico"] = request_["parameters"].get("proc9009_id_medico", 0)

            dtstring_ = str(request_["parameters"].get("data_exame", ""))
            hrstring_ = str(request_["parameters"].get("hora_exame_medico", ""))

            params_["data_exame"] = dtstring_[6:10] + "-" + \
                                    dtstring_[3:5] + "-" + \
                                    dtstring_[0:2] + "T00:00:00-00:00"

            params_["horario_exame"] = dtstring_[6:10] + "-" + \
                                       dtstring_[3:5] + "-" + \
                                       dtstring_[0:2] + "T" + hrstring_ + ":00-00:00"

            params_["codigo_ciretran_exame_psicologo"] = request_["parameters"].get("codigo_ciretran_psicologico", 0)
            params_["id_psicologo"] = request_["parameters"].get("proc9011_id_psicologo", 0)

            # ---------

            dtstring_ = str(request_["parameters"].get("data_exame_psicologico", ""))
            hrstring_ = str(request_["parameters"].get("hora_exame_psicologico", ""))

            params_["data_exame_psicologico"] = dtstring_[6:10] + "-" + \
                                                dtstring_[3:5] + "-" + \
                                                dtstring_[0:2] + "T00:00:00-00:00"

            params_["horario_exame_psicologico"] = dtstring_[6:10] + "-" + \
                                                   dtstring_[3:5] + "-" + \
                                                   dtstring_[0:2] + "T" + hrstring_ + ":00-00:00"
            # ---------

            params_["renach"] = request_["parameters"].get("renach", "SP000003189")
            params_["id_micro_regiao_medico"] = int(request_["parameters"].get("long_id", 0))

            params_["id_micro_regiao_psicologo"] = 0
            params_["usuario"] = request_["service"].get("canal").upper()

            context_ = await Consumers.servRealizarAgendamentoMedicoPsicologico(params_, request_["service"])

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        if context_ == {}:

            return {
                "text": "api_nok",
                "context": {}
            }

        else:

            context_tratado_: dict = {}
            context_tratado_ = splitDict("proc9013_", context_)

            cod_ = int(context_.get("codigo", 0))

            if cod_ == 400:

                if context_["mensagem"] == "Existe agendamento efetuado para este candidato.":

                    retorno_ = {
                        'text': 'api_nok',
                        'context': context_tratado_
                    }

                else:

                    retorno_ = {
                        'text': 'api_erro',
                        'context': context_tratado_
                    }

            else:

                retorno_ = {
                    'text': 'api_ok',
                    'context': context_tratado_
                }

        retorno_["context"]["process"] = ""

        return retorno_
