from api.utilities import fetchGET
from common.utils import Formatted
from common.cpf_cnpj_validator import ValidaCpfCnpj

validator: ValidaCpfCnpj = ValidaCpfCnpj()


class ServiceConsultaCadastro:

    @staticmethod
    async def serv_consulta_cadastro(request) -> dict:
        """
        nome: serv_consulta_cadastro
        :return: dict
        """

        url_: str
        headers_: dict
        params_: str

        try:
            url_ = request["service"].get("url") + "cpf/"

            headers_ = {
                "Authorization": "Bearer " + request["service"].get("token"),
                'Accepts': 'application/json',
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            cpf_ = Formatted(str(request["parameters"].get("cpf")))
            validator.get_cpf_cnpj(cpf_)

            if validator.valida():
                params_ = url_ + cpf_

            else:
                return {'code': 500,
                        'msg': 'CPF que você me informou é inválido'
                        }

        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)

        response_ = await fetchGET(params_, headers_)

        return response_
