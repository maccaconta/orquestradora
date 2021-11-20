from middle.consumers.consumers import Consumers


class Proc0009PostosPoupatempo(Consumers):

    @staticmethod
    async def get_postos_poupatempo(request_) -> dict:
        """
         name: get_postos_poupatempo
        :param request_: request
        :return: dict
        """

        _context: dict = {}
        _params: dict = {}
        context_tratado: dict = {}
        city: str = ""

        if request_["parameters"].get("cidade"):
            city = request_["parameters"].get("cidade")

        else:
            city = request_["parameters"].get("proc0006_municipio")

        _params["city"] = city
        _params["service_id"] = request_["parameters"]["idServico"]
        _params["organ_id"] = request_["parameters"]["idOrgao"]

        _context = await Consumers.serv_postos_poupatempo(_params, request_["service"])

        code = _context["code"]

        for i in range(6):
            context_tratado["proc0009_postos_disponiveis_" + str(i + 1)] = None

        if _context == {}:
            return {
                "text": "api_nok",
                "context":  _context
            }

        elif code == 0:
            if _context['post'] == []:
                return {
                    "text": "api_erro",
                    "context": {
                        "msg": "A cidade selecionada não possui posto que oferece este serviço."
                    }
                }

            for i in range(len(_context['post'])):
                context_tratado["proc0009_postos_disponiveis_" + str(i + 1)] =\
                    _context['post'][i]['description']

            context_tratado['process'] = ''

            return {
                "text": "api_ok",
                "context": context_tratado
            }

        elif code == 500:
            
            return {
                "text": "api_erro",
                "context": {"msg": "A cidade selecionada não possui posto que oferece este serviço."}
            }

        else:
            return {
                "text": "api_nok",
                "context": {}
            }
