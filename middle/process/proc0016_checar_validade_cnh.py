from middle.consumers.consumers import Consumers


class Proc0016ChecarValidadeCnh(Consumers):

    @staticmethod
    async def get_checar_validade_cnh(request_) -> dict:
        """
         name: get_checar_validade_cnh
        :param request_: request
        :return: dict
        """

        _context: dict = {}
        _params: dict = {}
        return_: dict = {}

        _params["cnh_data_vencimento"] = request_[
            "parameters"].get("cnh_data_vencimento", "")

        try:
            _context = await Consumers.serv_checar_validade_cnh(_params, request_["service"])

        except Exception as e:
            print(e)
        
        _context["process"] = ""

        return_ = {
            "text": "api_ok",
            "context": _context
        }

        return return_
