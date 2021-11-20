from api.utilities import splitDict, generate_numbers, createPDF, createPDFPadrao
from middle.consumers.serv_acesso_discovery import Discovery
import datetime as dt


class Proc5000AcessoDiscovery:

    def getDocumentDiscovery(request_) -> dict:
        """
        name: getDocumentDiscovery
        :param request_: request
        :return: dict
        """

        retorno_discovery_: dict = {}
        retorno_: dict = {}

        try:

            discovery_ = Discovery()

            if discovery_.connect():

                if discovery_.setCollection():

                    param_ = request_["parameters"].get("last_input", "") or request_["parameters"].get("user_input", "")

                    print('BUSCANDO NO DISCOVERY : ', request_["parameters"].get("last_input", "") , "/", request_["parameters"].get("user_input", ""))

                    retorno_discovery_ = discovery_.GetDocument(param_)

                try:

                    if "Não encontrei" in retorno_discovery_["texto_discovery"]:
                        retorno_ = {
                            'text': 'api_nok',
                            'context': retorno_discovery_
                        }
                    else:
                        retorno_ = {
                            'text': 'api_ok',
                            'context': retorno_discovery_
                        }
                except:
                    print(f"[ {dt.datetime.now()}] DISCOVERY NÃO ENCONTROU DOCUMENTOS!")
                    retorno_ = {
                        'text': 'api_nok',
                        'context': {"texto_discovery": "Não encontrei nenhum conteudo relevante para sua dúvida"}}

        except Exception as e:
            print(f"[ {dt.datetime.now()}] DISCOVERY NÃO ENCONTROU DOCUMENTOS!")

            retorno_ = {
                'text': 'api_nok',
                'context': {"texto_discovery": "Não encontrei nenhum conteudo relevante para sua dúvida"}}

            retorno_["context"]["process"] = ""

        return retorno_
