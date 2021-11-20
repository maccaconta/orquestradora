from middle.consumers.consumers import Consumers


class Proc9010RealizarAgendamentoMedicoRenovacao(Consumers):

    async def get_realizar_agendamento_medico_renovacao(request_) -> dict:
        """
        name: get_realizar_agendamento_medico_renovacao
        :param request_: request
        :return: dict
        """
        params_: dict = {}
        retorno_: dict = {}
        context_: dict = {}

        try:
            dtstring_ = str(request_["parameters"].get("data_exame", ""))
            dtstring_ = dtstring_[6:10] + "-" + \
                                    dtstring_[3:5] + "-" + \
                                    dtstring_[0:2]
            hstring = str(request_["parameters"].get("hora_exame_medico", ""))

            params_["cpf_cidadao"] = int(request_["parameters"].get("cpf", 0))
            params_["data_exame"] = dtstring_  + "T00:00:00-03:00"
            params_["tipo_processo"] = str(request_["parameters"].get("tipo_processo", "TODOS"))
            params_["cep_cidadao"] = int(request_["parameters"].get("proc9007_cep"))
            params_["categoria_pretendida"] = str(request_["parameters"].get("proc9007_categoria_atual", ""))
            params_["id_medico"] = int(request_["parameters"].get("proc9009_id_medico", 0))
            
            params_["horario_exame"] = dtstring_ + "T" + hstring  + ":00-03:00"
            params_["codigo_ciretran"] = int(request_["parameters"].get("codigo_ciretran", 0))
            params_["renach"] = request_["parameters"].get("proc9007_renach", "")
            params_["id_micro_regiao_medico"] = int(request_["parameters"].get("proc9027_long_id", 0))
            params_["usuario"] = "PORTAL" #str(request_["parameters"].get("usuario", ""))
            
            context_ = await Consumers.serviceRealizarAgendamentoMedicoRenovacao(params_, request_["service"])

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
                        "proc9010_mensagem": context_['mensagem']
                    }
                
                }
            
            elif cod_ == 500:
                retorno_ = {
                    'text': 'api_nok',
                    'context': context_
                }

            else:
                retorno_ = {
                    'text': 'api_ok',
                    'context': context_
                }

        return retorno_
