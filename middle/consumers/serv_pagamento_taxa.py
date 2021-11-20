from api.models import TaxPayment
from asgiref.sync import sync_to_async


class ServicePagtoTaxa:

    @staticmethod
    async def serv_pagamento_taxa(params, service) -> dict:
        """
        nome: serv_pagamento_taxa
        :return: ...
        """

        headers_: dict = {}
        return_: dict = {}

        print(service)

        # tax = await get_tax(params["tax_type"])
        tax = await sync_to_async(TaxPayment.objects.get)(tax_type=params["tax_type"])

        headers_ = {
            'Authorization': "Bearer " + service.get("token"),
            'Cache-Control': "no-cache",
            'Content-Type': "application/json; charset=UTF-8",
            'Accept': "*/*",
            'Connection': "keep-alive"
        }

        print("Parâmetros da requisição:", params)

        return_ = {
            "valor_taxa": str(tax.tax_value),
            "nome_taxa": str(tax.tax_name)
        }        

        return return_

    @sync_to_async
    def get_tax(tax_type):
        return TaxPayment.objects.get(tax_type)
