from api.utilities import splitDict, createPDF, generator
from middle.consumers.consumers import Consumers
from decouple import config


class Proc0003AntecedentesCriminais(Consumers):

    async def get_antecedentes_criminais(request_) -> dict:
        """
         name: get_antecedentes_criminais
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}

        try:
            params_["rg"] = str(request_["parameters"].get("proc0002_RG", " "))
            params_["digito"] = str(request_["parameters"].get("proc0002_digito", " "))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_antecedentes_criminais(params_, request_["service"])

        if context_ == {} or not context_:
            return {
                "text": "api_nok",
                "context": {}
            }
        if 'code' in context_:
            return {
                "text": "api_erro",
                "context": {
                    "proc0003_msg": context_,
                    "process": ""
                }
            }
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc0003_", context_)

                file_name = generator()
                link_ = createPDF(context_tratado_["proc0003_pdfBase64"], str(file_name))

                return {
                    'text': 'api_ok',
                    'context': {
                        'link_antecedente': config('ORCHEST_URL_PUBLIC') + "/" + link_ + ".pdf",
                        'process': ""
                    }
                }

            except Exception as e:
                print("Falha na atualização da matrix", e)
                return {
                    'text': 'api_nok',
                    'context': {}
                }
