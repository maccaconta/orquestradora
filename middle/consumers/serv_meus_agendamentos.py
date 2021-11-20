from api.utilities import fetchGET
from common.utils import Formatted
from common.cpf_cnpj_validator import ValidaCpfCnpj

validator: ValidaCpfCnpj = ValidaCpfCnpj()


class ServiceMeusAgendamentos:

    @staticmethod
    async def serv_meus_agendamentos(request) -> dict:
        """
        nome: serv_meus_agendamentos
        :return: dict
        """

        url_: str
        headers_: dict
        cpf_: str

        try:
            url_ = request["service"].get("url") + "/v1/agendas/agenda/"

            headers_ = {
                "Authorization": "Bearer " + request["service"].get("token")
            }

            cpf_ = Formatted(str(request["parameters"].get("cpf")))
            validator.get_cpf_cnpj(cpf_)
            if validator.valida():
                fetch_ = url_ + cpf_

            else:
                return {'code': 500,
                        'msg': 'CPF inválido'
                        }

        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)

        response_ = await fetchGET(fetch_, headers_)

        return response_
