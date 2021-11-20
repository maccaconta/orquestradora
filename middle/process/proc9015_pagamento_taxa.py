from middle.consumers.consumers import Consumers
from api.utilities import splitDict


class Proc9015TaxaPagtoCNH(Consumers):

    @staticmethod
    async def get_valores_taxa(request_) -> dict:
        """
         name: get_valores_taxa
        :param request_: request
        :return: dict
        """

        _context: dict = {}
        _params: dict = {}
        _return: dict = {}

        _params["tax_type"] = request_["parameters"]["tax_type"]

        _context = await Consumers.serv_pagamento_taxa(_params, request_["service"])

        print("context:", _context)

        if _context == {}:
            return {
                "text": "api_nok",
                "context": {}
            }
        else:

            return {
                "text": "api_ok",
                "context": _context
            }