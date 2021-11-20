from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9005ConsultarRG(Consumers):

    async def getConsultarRG(request_) -> dict:
        """
        name: getConsultarRG
        :param request_: request
        :return: dict
        """

        # Todo : não conseguimos ainda testar

        params_: dict = {}
        retorno_: dict = {}
        context_: dict = {}
        data_: dict = {}

        try:
            rg = str(request_["parameters"].get("numero_rg", 0))
            tamanho  =  len(rg)           
            params_["rg"] = rg[:tamanho]
            params_["digito_rg"] = rg[tamanho-1:]

            dtstring_ = str(request_["parameters"].get("data_emissao_rg", ""))

            if len(dtstring_) == 10:
                params_["data_expedicao"] = dtstring_[6:10] + "-" + dtstring_[3:5] + "-" + dtstring_[0:2]
            else:
                params_["data_expedicao"] = ""


            params_["cpf"] = str(request_["parameters"].get("cpf", 0))

            context_ = await Consumers.servConsultaRG(params_, request_["service"])

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        if context_ == {}:

            return {
                "text": "api_nok",
                "context": {}
            }

        else:

            context_tratado_: dict = {}
            context_tratado_ = splitDict("proc9005_", context_)

            cod_ = int(context_.get("codigo", 0))

            if cod_ == 400 or cod_ == 204:

                retorno_ = {
                    'text': 'api_erro',
                    'context': context_tratado_
                }

            elif cod_ == 1603:

                retorno_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }

            elif cod_ == 201:
                retorno_ = {
                    'text': 'api_ok',
                    'context': context_tratado_
                }

        retorno_["context"]["process"] = ""

        return retorno_
