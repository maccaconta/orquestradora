
class ServiceBuscaEndereco:

    @staticmethod
    def serv_busca_endereco(request) -> dict:
        """
        nome: serv_busca_endereco
        :return: ...
        """

        # if (request["cep"]):

        json_ = {
            "codigo": "123",
            "cep": 12345678,
            "logradouro": "Rua ASfdf",
            "numero": 2,
            "complemento": "fundos",
            "bairro": "Pinheiros",
            "cidade": "São Paulo",
            "uf": "SP",
            "retorno": "ok"
        }

        return json_