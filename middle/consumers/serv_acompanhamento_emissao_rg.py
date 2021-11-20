from api.utilities import fetchPOST
from common.rg_validator import ValidaRg
import re
from common.cpf_cnpj_validator import ValidaCpfCnpj


validatorRg: ValidaRg = ValidaRg()
validator: ValidaCpfCnpj = ValidaCpfCnpj()


class ServiceAcompanhamentoEmissaoRg:

    @staticmethod
    async def serv_acompanhamento_emissao_rg(param, service) -> dict:
        """
        nome: serv_acompanhamento_emissao_rg
        :return: ...
        """

        url_: str = ""
        _cpf: str = ""
        _rg: str = ""
        headers_: dict = {}
        retorno_: dict = {}

        try:
            url_ = service.get("url") + "/statusEmissaoRG"

            headers_ = {
                'Authorization': "Bearer " + service.get("token"),
                'Cache-Control': "no-cache",
                'Content-Type': "application/json",
                'Accept': "*/*",
                'Connection': "keep-alive"
            }
            
            pattern = re.compile("[\.\-]", re.IGNORECASE)
            _cpf = pattern.sub('', str(param["cpfNumero"]) + str(param["cpfDigito"]))
            _rg = str(param["registroNumero"]) + str(param["registroDigito"])
            validatorRg.set_rg(_rg)
            validator.get_cpf_cnpj(_cpf)

            if validator.valida() and validatorRg.valida_rg():
                retorno_ = await fetchPOST(url_, param, headers_)

            if not validatorRg.valida_rg() or not validator.valida():
                document = "CPF" if not validator.valida() else "RG"
                return {'code': 500,
                        'proc0007_msg': f'O {document} que você me informou é inválido.',
                        'document': document
                        }
            print("Parâmetros da requisição:", param)

        except Exception as e:

            print("Dados da requisição não foram enviados para consulta do serviço", e)

        return retorno_
