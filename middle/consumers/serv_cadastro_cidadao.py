import json
import time


class ServiceCadastroCidadao:

    @staticmethod
    def serv_cadastro_cidadao(request) -> dict:
        """
         name: serv_cadastro_cidadao
        :param request: request
        :return: dict, retorno_
        """
        """
        name: serv_cadastro_cidadao
        service: consumidor do serviço Detran de Cadastro de Cidadão
        cpf, nome, validade, restrições
        """

        time.sleep(1)
        cpf_ = request["parameters"]["cpf"]

        if cpf_ == 123456:
            nome_ = 'Marcelo Maccaferri'
        else:
            nome_ = "outra pessoa"

        retorno_: dict = {

            'cpf': + request["parameters"]["cpf"],
            'nome': nome_,
            'validade': '10/10/2025',
            'restricoes': 'não possui'
        }

        return retorno_

