from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
from decouple import config
import datetime as dt

import traceback
import datetime as dt

import json


class Discovery:

    def __init__(self) -> object:
        self.url: str = config('DISCOVERY_URL')
        self.apikey: str = config('DISCOVERY_APIKEY')
        self.projectID: str = config('DISCOVERY_PROJECTID')
        self.collection: str = config('DISCOVERY_COLLECTION_ID')
        self.discovery = None
        self.ColletionID: list = []
        self.authenticator = None

    def connect(self):

        try:
            self.authenticator = IAMAuthenticator(self.apikey)
            self.discovery = DiscoveryV2(
                version='2020-08-30',
                authenticator=self.authenticator
            )

            self.discovery.set_service_url(self.url)

            return True

        except:
            return False

    def setCollection(self):

        try:
            response = self.discovery.list_collections(
                project_id=self.projectID
            ).get_result()

            retorno_ = json.dumps(response, indent=2)

            # response[1]['collection_id']
            # response["collections"]
            print('...VERIFICANDO DISCOVERY COLLECTIONS ', retorno_)

            return True
        except:
            return False

    def GetDocument(self, texto):

        try:

            query_result = self.discovery.query(
                project_id=f'{self.projectID}',
                collection_ids=[f'{self.collection}'],
                natural_language_query=f'{texto}',
                highlight=True,
                passages={
                    "enabled": True,
                    "per_document": True,
                    "find_answers": True
                }
                # count=1
            )

            answer_mais_relevante = ""
            resultado = query_result.result

            num_docs_relevantes = resultado['matching_results']
            # print(f"[ {dt.datetime.now()}] DISCOVERY - numero de documentos relevantes:", num_docs_relevantes)

            try:
                document_mais_relevante = resultado['results'][0]
                passagens = resultado['results'][0]['document_passages']

                passagem_mais_relevante = passagens[0]
                documento_id_mais_relevante = document_mais_relevante['document_id']
                try:
                    score_id_mais_relevante = passagem_mais_relevante['answers'][0]['confidence']
                except:
                    score_id_mais_relevante = 0

                try:
                    answer_mais_relevante = passagem_mais_relevante['answers'][0]["answer_text"]
                except:
                    answer_mais_relevante = ""

                try:
                    texto_relevante = passagem_mais_relevante["passage_text"]
                except:
                    texto_relevante = ""

                if answer_mais_relevante=="":
                    texto =  texto_relevante
                else:
                    texto = answer_mais_relevante

                print(resultado['results'][0])
                print ("answer_mais_relevante", answer_mais_relevante)
                print("passagem_mais_relevante", passagem_mais_relevante)

                if score_id_mais_relevante > 0.1: #or texto != ""
                    return {
                        "texto_discovery": texto,
                        "passagens": passagens,
                        "score": score_id_mais_relevante
                    }
                else:
                    return {"texto_discovery": "Não encontrei nenhum conteudo relevante para sua dúvida",
                            "passagens": "",
                            "score": 0}

            except Exception:
                return {}

        except ApiException as e:
            return {"texto_discovery": "Não encontrei nenhum conteudo relevante para sua dúvida",
                    "passagens": "",
                    "score": 0}


