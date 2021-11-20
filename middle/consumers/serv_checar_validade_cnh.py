from datetime import datetime, timedelta, date


class ServiceChecarValidadeCnh:

    @staticmethod
    async def serv_checar_validade_cnh(params, service) -> dict:
        """
        nome: serv_checar_validade_cnh
        :return: ...
        """
        return_: dict = {}
        cnh_data_vencimento: str = ""

        try:
            data_vencimento = str(params["cnh_data_vencimento"])
            cnh_data_vencimento = datetime.strptime(
                data_vencimento, "%d/%m/%Y")
            data = datetime.now() + timedelta(days=30)

            validated_data = cnh_data_vencimento > data

            return_ = {'validated_data': validated_data}

        except Exception as e:

            print("Dados da requisição não foram enviados para consulta do serviço", e)

        return return_
