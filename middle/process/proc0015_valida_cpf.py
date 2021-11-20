from middle.consumers.consumers import Consumers


class Proc0015ValidaCpf(Consumers):

    @staticmethod
    async def get_valida_cpf(request_) -> dict:
        """
         name: get_valida_cpf
        :param request_: request
        :return: dict
        """

        _context: dict = {}
        _params: dict = {}

        _params["cpf"] = request_["parameters"].get("cpf", "")

        _context = await Consumers.serv_valida_cpf(_params)
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