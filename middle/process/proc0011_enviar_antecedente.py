from api.utilities import splitDict, createPDF, generator
from middle.consumers.consumers import Consumers
from decouple import config


class Proc0011EnviarAntecedente(Consumers):

    async def get_enviar_antecedente(request_) -> dict:
        """
         name: get_enviar_antecedente
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            params_["rg"] = str(request_["parameters"].get("proc0002_RG", ""))
            params_["digito"] = str(request_["parameters"].get("proc0002_digito", ""))
            params_["email"] = str(request_["parameters"].get("proc0002_Email", ""))
            params_["tipo"] = "AMBOS"

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_enviar_antecedente(params_, request_["service"])
        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }
        elif not params_.get('email'):
            return {
                "text": "api_erro",
                "context": {
                    "proc0011_msg": "Email Vazio, por favor verifique o parâmetro"
                    }
            }
        else:

            context_tratado_: dict = {}
            context_tratado_ = splitDict("proc0011_", context_)

            file_name = generator()
            link_ = createPDF(
                context_tratado_["proc0011_pdfBase64"], str(file_name))

            return_ = {
                'text': 'api_ok',
                'context': {
                    'link_enviar_antecedente': config('ORCHEST_URL_PUBLIC') + "/" + link_ + ".pdf"
                }
            }

        return_["context"]["process"] = ""
        return return_
