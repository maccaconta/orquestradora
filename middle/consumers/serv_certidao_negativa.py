from api.utilities import fetchPOST
from common.cpf_cnpj_validator import ValidaCpfCnpj


validatorCpf: ValidaCpfCnpj = ValidaCpfCnpj()


class ServiceCertidaoNegativa:

    @staticmethod
    async def serv_certidao_negativa(data, service) -> dict:
        """
        nome: serv_certidao_negativa
        :return: ...
        """

        url_: str
        headers_: dict = {}
        retorno_: dict = {}

        try:
            url_ = service.get("url") + "certidao-negativa/2/" + \
                   data
            headers_ = {
                'Authorization': "Bearer " + service.get("token"),
                'Cache-Control': "no-cache",
                'Content-Type': "application/json; charset=UTF-8",
                'Accept': "*/*",
                'Cookie': "ROUTEID=.2"
            }
            
            print("Parâmetros da requisição:", data)
            validatorCpf.get_cpf_cnpj(data)

            if validatorCpf.valida():
                retorno_ = await fetchPOST(url_, {}, headers_)
                # print("Retorno da API:", retorno_)
            else:
                return {'code': 500,
                        'Mensagem': 'CPF inválido'
                        }

        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)

        return retorno_

