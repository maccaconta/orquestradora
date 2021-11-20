from middle.consumers.consumers import Consumers


class Proc0004DataAgendamentoPoupatempo(Consumers):

    async def get_data_agendamento_poupatempo(request_) -> dict:
        """
         name: get_data_agendamento_poupatempo
        :param request_: request
        :return: dict
        """
        data_: dict = {}
        context_: dict = {}

        try:
            context_ = await Consumers.serv_data_agendamento_poupatempo(request_)
        except Exception as e:
            print("Erro ", e)
        if type(context_) is str:

            if "Agendamento não realizado" in context_ or "eagenda.persistencia.exception.DaoException:" in context_ :
               
                return {
                    "text": "api_erro",
                    "context": {
                        'msg_proc0004': context_,
                        'process': ""
                    }
                }

        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {
                    "process": ""
                }
            }

        else:
            try:
                for i in range(len(context_)):
                    data_["proc0004_data_disponiveis_" + str(i + 1)] = \
                        str(context_[i][-2:]) + "/" + \
                        str(context_[i][-4:-2]) + "/" + \
                        str(context_[i][-8:-4])
                data_['process'] = ''
                return {
                    "text": "api_ok",
                    "context": data_

                }
            except Exception as e:
                print("error", e)

