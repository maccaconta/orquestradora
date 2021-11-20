from common.rg_validator import ValidaRg
from common.utils import Formatted


validatorRg: ValidaRg = ValidaRg()


class ServiceValidaRg:

    @staticmethod
    async def serv_valida_rg(params) -> dict:
        """
        nome: serv_valida_rg
        :return: ...
        """
        return_: dict = {}
        rg_: str = ""

        try:

            rg_ = Formatted(str(params["rg"]))
            validatorRg.set_rg(rg_)
            validatorRg.valida_rg()

            if validatorRg.valida_rg():
                return_ = {'code': 0,
                           }

            else:
                return_ = {'code': 500,
                           'proc0017_msg': 'O RG que você me informou é inválido.'
                           }

        except Exception as e:

            print("Dados da requisição não foram enviados para consulta do serviço", e)

        return return_
