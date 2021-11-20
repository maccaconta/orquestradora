

class ServiceCadastroCepEndereco:

    @staticmethod
    def serv_cadastro_cep_endereco(request) -> dict:
        """
        nome: serv_cadastro_cep_endereco
        :return: ...
        """

        if (request["cep"] and request["numero_logradouro"] and request["logradouro"]
                and request["complemento"] and request["bairro"] and request["municipio"]):

            json_ = {
                "codigo": 0,
                "mensagem": "tudo ok"
            }

        return json_