from common.utils import Formatted
from common.cpf_cnpj_validator import ValidaCpfCnpj


validator: ValidaCpfCnpj = ValidaCpfCnpj()


class ServiceValidaCpf:

    @staticmethod
    async def serv_valida_cpf(params) -> dict:
        """
        nome: serv_valida_cpf
        :return: ...
        """
        return_: dict = {}
        cpf_: str = ""

        try:

            cpf_ = Formatted(str(params["cpf"]))
            validator.get_cpf_cnpj(cpf_)
            validator.valida()

            if validator.valida():
                return_ = {'code': 0,
                           }

            else:
                return_ = {'code': 500,
                           'proc0015_msg': 'O CPF que você me informou é inválido.'
                           }

        except Exception as e:

            print("Dados da requisição não foram enviados para consulta do serviço", e)

        return return_
