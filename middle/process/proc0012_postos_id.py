from middle.consumers.consumers import Consumers


class Proc0012PostosId(Consumers):

    @staticmethod
    async def get_postos_id(request_) -> dict:
        """
         name: get_postos_poupatempo
        :param request_: request
        :return: dict
        """

        _context: dict = {}
        _params: dict = {}

        _params["description"] = request_["parameters"]["postos_sp"]
        _params["organ_id"] = request_["parameters"].get("idOrgao", "")

        _context = await Consumers.serv_postos_id(_params, request_["service"])
        code = _context["code"]
   
        _context['process'] = ''

        if _context == {}:
            return {
                "text": "api_erro",
                "context": {}
            }
        elif _context["service"] == [] or "Parâmetro local não foi informado corretamente" in _context["service"]:
            msg = "Esse posto Poupatempo não oferece esse serviço."
            _context["msg"] = msg
            return {
                "text": "api_erro",
                "context":_context
                            
                            
            }
        elif code == 0:

            return {
                "text": "api_ok",
                "context": _context
            }

        elif code == 500:
            return {
                "text": "api_nok",
                "context": _context
            }
        else:
            return {
                "text": "api_nok",
                "context": {}
            }
