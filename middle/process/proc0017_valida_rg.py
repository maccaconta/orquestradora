from middle.consumers.consumers import Consumers


class Proc0017ValidaRg(Consumers):

    @staticmethod
    async def get_valida_rg(request_) -> dict:
        """
         name: get_valida_rg
        :param request_: request
        :return: dict
        """

        _context: dict = {}
        _params: dict = {}

        _params["rg"] = request_["parameters"].get("rg", "")

        _context = await Consumers.serv_valida_rg(_params)
        print(_context)

        if _context["code"] == 500:

            return {
                "text": "api_erro",
                "context": _context
            }

        else:
            return {
                "text": "api_ok",
                "context": {}
            }
