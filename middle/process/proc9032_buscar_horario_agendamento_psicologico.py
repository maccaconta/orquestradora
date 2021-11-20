from middle.consumers.consumers import Consumers


class Proc9032BuscarHorarioAgendamentoPsicologico(Consumers):

    async def get_buscar_horario_agendamento_psicologico(request_) -> dict:
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

            dtstring_ = str(request_["parameters"].get("data_exame_psicologico", ""))

            if len(dtstring_) == 10:
                params_["data_exame_psicologico"] = dtstring_[6:10] + "-" + \
                                                    dtstring_[3:5] + "-" + \
                                                    dtstring_[0:2] + "T00:00:00-00:00"

            if str(request_["parameters"].get("data_exame", "")) == "":
                params_["existe_agendamento_exame_medico"] = False
            else:
                params_["existe_agendamento_exame_medico"] = True

            params_["id_psicologo"] = int(request_["parameters"].get("proc9011_id_psicologo", 0))

            context_ = await Consumers.serv_buscar_horario_agendamento_psicologico(params_, request_["service"])

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        if context_ == {}:

            return {
                "text": "api_nok",
                "context": {}
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
                try:

                    for i in range(len(context_["horarios_disponiveis"])):
                        data_["proc9032_horarios_disponiveis_" + str(i + 1)] = \
                            context_["horarios_disponiveis"][i][11:16:1]

                    data_["proc9032_id_psicologo"] = context_["id_medico"]

                    retorno_ = {
                        'text': 'api_ok',
                        'context': data_
                    }

                except:

                    retorno_ = {
                        'text': 'api_nok',
                        'context': {
                            "mensagem": context_['mensagem']
                        }
                    }

        retorno_["context"]["process"] = ""

        return retorno_
