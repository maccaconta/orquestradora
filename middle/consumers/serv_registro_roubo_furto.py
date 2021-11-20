
class ServiceRegistroRouboFurto:

    @staticmethod
    def serv_registro_roubo_furto(request) -> dict:
        """
        name: ser_registro_roubo_furto
        :param request_: request
        :return: dict
        """
        if (request["placa"]):

            json_ = {
                "placa": "123",
                "marca": "bla",
                "ano_fabricacao": "1992",
                "ano_modelo": "1993",
                "cor": "preto"
            }

        return json_
