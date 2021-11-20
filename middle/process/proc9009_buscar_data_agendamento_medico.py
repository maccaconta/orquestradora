from middle.consumers.consumers import Consumers


class Proc9009BuscarDataAgendamentoMedico(Consumers):

    async def get_buscar_data_agendamento_medico(request_) -> dict:
        """
        name: get_buscar_data_agendamento_medico
        :param request_: request
        :return: dict
        """
        params_: dict = {}
        retorno_: dict = {}
        context_: dict = {}
        data_: dict = {}

        try:

            params_["cpf_cidadao"] = int(request_["parameters"].get("cpf", ""))
            params_["codigo_ciretran"] = int(request_["parameters"].get("codigo_ciretran", 0))
            params_["usuario"] = request_["service"].get("canal").upper()

            params_["is_portador_necessidades_especiais"] = True \
                if str(request_["parameters"].get("is_portador_necessidades_especiais", "SIM")).upper() == "SIM" \
                else False

            params_["cep_cidadao"] = int(request_["parameters"].get("cep"))
            params_["id_micro_regiao"] = int(request_["parameters"].get("proc9027_long_id", ""))

            context_ = await Consumers.serv_buscar_data_agendamento_medico(params_, request_["service"])

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
                        data_["proc9009_data_disponiveis_" + str(i + 1)] = \
                            context_["datas_disponiveis"][i][8:10] + "/" + \
                            context_["datas_disponiveis"][i][5:7] + "/" + \
                            context_["datas_disponiveis"][i][0:4]

                    data_["proc9009_id_medico"] = context_["id_medico"]

                except:

                    for i in range(len(context_["unidades_disponiveis"])):
                        data_["proc9009_codigo_ciretran_" + str(i + 1)] = \
                            context_["unidades_disponiveis"][i].get("codigo_ciretran")

                        data_["proc9009_nome_unidade_" + str(i + 1)] = \
                            context_["unidades_disponiveis"][i].get("nome_unidade")

                retorno_ = {
                    'text': 'api_ok',
                    'context': data_
                }

        retorno_["context"]["process"] = ""

        return retorno_
