from middle.consumers.consumers import Consumers


class Proc0001MeusAgendamentos(Consumers):

    async def get_meus_agendamentos(request_) -> dict:
        """
         name: get_meus_agendamentos
        :param request_: request
        :return: dict
        """
        treatment_: dict = {}

        try:
            _context = await Consumers.serv_meus_agendamentos(request_)
        except Exception as e:
            print("Erro no Context", e)
        if _context == {} or not _context:
            return {
                "text": "api_nok",
                "context": {}
            }
        elif 'code' in _context and _context['code'] == 500:
            return {
                "text": "api_erro",
                "context": _context
            }
        else:
            try:
                for i in range(len(_context)):
                    treatment_["Agendamento_" + str(i + 1)] = {
                        "Servico": _context[i]["servico"]["nome"],
                        "Unidade": _context[i]["local"]["nome"],
                        "Endereco": _context[i]["local"]["endereco"],
                        "Data": _context[i]["horaini"][-6:-4] + '/' + _context[i]["horaini"][-8:-6] + '/' + _context[i][
                                                                                                                "horaini"][
                                                                                                            -12:-8],
                        "Horarios": _context[i]["horaini"][-4:-2] + ':' + _context[i]["horaini"][-2:],
                        "Protocolo": _context[i]["protocolo"]
                    }
                
            except Exception as e:
                print("Erro no filtro do  Context", e)

            return {
                "text": "api_ok",
                "context": treatment_

            }
