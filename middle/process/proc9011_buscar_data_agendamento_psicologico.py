from middle.consumers.consumers import Consumers


class Proc9011BuscarDataAgendamentoPsicologico(Consumers):

    async def get_buscar_data_agendamento_psicologico(request_) -> dict:
        """
        name: get_buscar_data_agendamento_psicologico
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        retorno_: dict = {}
        context_: dict = {}
        data_: dict = {}
        busca_data_: bool = False

        try:

            params_["cpf_cidadao"] = str(request_["parameters"].get("cpf", ""))

            try:
                params_["codigo_ciretran"] = int(request_["parameters"].get("codigo_ciretran_psicologico", 0))
            except:
                params_["codigo_ciretran"] = 0

            if params_["codigo_ciretran"] != 0:
                busca_data_ = True
            else:
                busca_data_= False

            params_["usuario"] = request_["service"].get("canal").upper()

            params_["cep_cidadao"] = str(request_["parameters"].get("cep"))
            params_["id_micro_regiao"] = int(request_["parameters"].get("proc9027_long_id", ""))

            dtstring_ = str(request_["parameters"].get("data_exame", ""))
            hrstring = request_["parameters"].get("hora_exame_medico", "")

            if len(dtstring_) == 10:
                params_["data_exame_medico"] = dtstring_[6:10] + "-" + \
                                               dtstring_[3:5] + "-" + \
                                               dtstring_[0:2] + "T" + \
                                               hrstring + ":00-00:00"

                params_["horario_exame_medico"] = dtstring_[6:10] + "-" + \
                                                  dtstring_[3:5] + "-" + \
                                                  dtstring_[0:2] + "T" + \
                                                  hrstring + ":00-00:00"
            else:
                params_["data_exame_medico"] = ""

            context_ = await Consumers.serv_buscar_data_agendamento_psicologico(params_, request_["service"])

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
                try:

                    for i in range(len(context_["datas_disponiveis"])):
                        data_["proc9011_datas_disponiveis_" + str(i + 1)] = \
                            context_["datas_disponiveis"][i][8:10] + "/" + \
                            context_["datas_disponiveis"][i][5:7] + "/" + \
                            context_["datas_disponiveis"][i][0:4]

                    data_["proc9011_id_medico"] = context_["id_medico"]
                    data_["proc9011_id_psicologo"] = context_["id_psicologo"]
                    data_["proc9011_tipo_retorno"] = "datas_disponiveis"

                    retorno_ = {
                        'text': 'api_ok',
                        'context': data_
                    }

                except:

                    if busca_data_:

                        retorno_ = {
                            'text': 'api_erro',
                            'context': {}
                        }

                    else:
                        for i in range(len(context_["unidades_disponiveis"])):
                            data_["proc9011_codigo_ciretran_" + str(i + 1)] = \
                                context_["unidades_disponiveis"][i].get("codigo_ciretran")

                            data_["proc9011_nome_unidade_" + str(i + 1)] = \
                                context_["unidades_disponiveis"][i].get("nome_unidade")

                            data_["proc9011_tipo_retorno"] = "unidades_disponiveis"

                            retorno_ = {
                                'text': 'api_ok',
                                'context': data_
                            }

        retorno_["context"]["process"] = ""

        return retorno_
