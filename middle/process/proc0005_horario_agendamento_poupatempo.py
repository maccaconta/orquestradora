from middle.consumers.consumers import Consumers


class Proc0005HorarioAgendamentoPoupatempo(Consumers):

    async def get_horario_agendamento_poupatempo(request_) -> dict:
        """
         name: get_data_agendamento_poupatempo
        :param request_: request
        :return: dict
        """
        horarios = []
        _context: dict = {}
        tratado_hora_: dict = {}
        periodo: dict = {}
        horas = []

        try:

            _context = await Consumers.serv_horario_agendamento_poupatempo(request_)
            periodo = str(request_["parameters"].get("periodo", ""))

            for i in range(len(_context)):
                horarios.append(int(_context[i]['horario']))

        except Exception as e:
            print("Erro ", e)

        if _context == {} or not _context:
            return {
                "text": "api_nok",
                "context": {
                    "process": ""
                }
            }
        elif 'code' in _context and _context['code'] == 400:

            return {
                "text": "api_erro",
                "context": _context,
                "process": ""
            }
        else:
            try:
                if periodo == 'Periodo_Manha':
                    for i in range(len(horarios)):
                        if (horarios[i]) <= 1200:
                            horas.append(str((horarios[i])))
                elif periodo == 'Periodo_Tarde':
                    for i in range(len(horarios)):
                        if (horarios[i]) > 1200:
                            horas.append(str((horarios[i])))
                
                if len(horas) > 0:
                    tratado_hora_['msg'] = 'Ok, agora escolha um dos horários disponíveis para o período escolhido'
                    for i in range(len(horas)):
                        if len(horas[i]) == 3:
                            tratado_hora_["proc0005_horarios_disponiveis_" + str(i + 1)] = '0' + \
                                                                                        horas[i][:1] + \
                                ':' + horas[i][1:3]
                        else:
                            tratado_hora_["proc0005_horarios_disponiveis_" + str(i + 1)] = \
                                horas[i][:2] + ':' + horas[i][2:4]
                else:
                    tratado_hora_ = { 
                        "msg": "Não encontrei horário para período selecionado nesta data. Para prosseguir escolha outra data, posto ou período."
                    }

            except Exception as e:
                print(e)
                return {
                    "text": "api_nok",
                    "context": {
                        "process": ""
                    }
                }

            return {
                'text': 'api_ok',
                'context': tratado_hora_,
                "process": ""
            }
