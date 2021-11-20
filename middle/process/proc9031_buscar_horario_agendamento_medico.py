from api.utilities import splitDict
from middle.consumers.consumers import Consumers
import datetime


class Proc9031BuscarHorarioAgendamentoMedico(Consumers):

    async def get_buscar_horario_agendamento_medico(request_) -> dict:
        """
        name: get_buscar_horario_agendamento_medico
        :param request_: request
        :return: dict
        """

        context_: dict = {}
        retorno_: dict = {}
        params_: dict = {}

        try:

            dtstring_ = str(request_["parameters"].get("data_exame", ""))

            if len(dtstring_) == 10:
                params_["data_exame"] = dtstring_[6:10] + "-" + dtstring_[3:5] + "-" + dtstring_[0:2] + "T00:00:00-03:00"
            else:
                params_["data_exame"] = ""

            params_["id_medico"] = str(request_["parameters"].get("proc9009_id_medico", ""))

            context_ = await Consumers.serv_buscar_horario_agendamento_medico(params_, request_["service"])

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        if context_ == {}:
            retorno_ = {
                "text": "api_nok",
                "context": {}
            }
        else:

            context_tratado_: dict = {}
            context_tratado_ = splitDict("proc9031_", context_)

            context_tratado_["proc_31_manha"] = "nao"
            context_tratado_["proc_31_tarde"] = "nao"

            for context_pai_key_, context_pai_val_ in context_tratado_.items():

                try:

                    hora_ = int(context_pai_val_[11:13:1])
                    hora_min_ = context_pai_val_[11:16:1]

                    if int(hora_) <= 12:
                        context_tratado_["proc_31_manha"] = "sim"

                    if int(hora_) > 12:
                        context_tratado_["proc_31_tarde"] = "sim"

                    context_tratado_[context_pai_key_] = hora_min_

                except:
                    pass

            retorno_ = {
                'text': 'api_ok',
                'context': context_tratado_
            }

        return retorno_