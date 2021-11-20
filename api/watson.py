from django.core.exceptions import ObjectDoesNotExist
from ibm_watson import AssistantV2
from ibm_watson import ApiException
from django.conf import settings
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.authenticators import CloudPakForDataAuthenticator
from api.orchestrator.event_models.bulk import EventModelBulk
import datetime as dt
import urllib3
urllib3.disable_warnings()


#
# Class: Watson
# Função: mensageria com o IBM Watson Assist
# Métodos: sendWatson
#

class Watson(EventModelBulk):

    def __init__(self):
        self.session: str = ''
        self.intent: str = ''
        self.answer = None
        self.status: int = 0
        self.confidence: int = 0
        self.assistant = None
        self.connected: bool = False
        self.assistant_id: str = ''
        self.credentials: dict = {}

    #
    # Estabelece conexão com Watson
    #

    def connect(self, watson: dict) -> bool:
        """
         name: connect
        :return: bool
        """

        self.credentials = watson

        try:
            # if not self.connected:
            self.accreditation()

            self.connected = True
            return self.connected

        except ApiException as e:
            self.connected = False
            self.status = e.code
            self.answer = settings.MSG_ERROR + e.message
            return self.connected

    #
    # Envia mensagem para Watson
    #

    def send(self, session_id: str, msg: str, context_: dict) -> bool:
        """
         name: send
        :param session_id: str
        :param msg: str
        :param context_: dict
        :return: bool
        """

        attempts_: int = 0

        for attempts_ in range(1):
            try:

                print(f"[ {dt.datetime.now()}]  *** WATSON REQUEST - Texto Enviado: {str(msg)} / Contexto Enviado {context_}")

                response_: object

                if session_id == "":
                    if not self.newSession():
                        break
                else:
                    self.session = session_id

                response_ = self.assistant.message(
                    assistant_id=self.assistant_id,
                    session_id=self.session,
                    input={
                        'message_type': 'text',
                        'text': str(msg), 'options': {
                            'return_context': True,
                            'debug': True
                        }
                    },
                    context={
                        "skills": {
                            "main skill": {
                                "user_defined":
                                    context_

                            }
                        }
                    }
                ).get_result()

                print(f"[ {dt.datetime.now()}]  *** WATSON RESPONSE : {response_}")

                self.answer = response_
                self.answer["session"] = self.session

                return True

            except ApiException as e:
                session_id = ''
                self.status = e.code
                self.answer = settings.MSG_ERROR + e.message

        return False

    #
    # Destrói sessão criada
    #

    def deleteSession(self, session_id: str) -> bool:
        """
         name: deleteSession
        :param session_id: str
        :return: bool
        """
        try:
            response_ = self.assistant.delete_session(
                assistant_id=self.assistant_id,
                session_id=session_id
            ).get_result()

            return True

        except ApiException as e:
            self.status = e.code
            self.answer = settings.MSG_ERROR + e.message

            return False

    #
    # Abre nova sessão do Watson
    #

    def newSession(self) -> bool:
        """
         name: newSession
        :return: bool
        """
        try:

            session_ = self.assistant.create_session(self.assistant_id).get_result()
            self.session = session_['session_id']
            return True

        except ApiException as e:
            print(f"[ {dt.datetime.now()}]  !!! ERRO AO CRIAR SESSÃO NO WATSON ASSISTANT :", e)
            self.status = e.code
            self.answer = settings.MSG_ERROR + e.message

            return False

    def accreditation(self) -> bool:
        """
        name: newSession
        :return: bool
        """
        try:

            authenticator = BearerTokenAuthenticator(self.credentials["assistent_apikey"])

            #authenticator = IAMAuthenticator(self.credentials["assistent_apikey"])

            self.assistant = AssistantV2(
                version=self.credentials["assistent_version"],
                authenticator=authenticator
            )
            self.assistant.set_service_url(self.credentials["assistent_url"])
            self.assistant_id = self.credentials["assistent_id"]

            self.assistant.set_disable_ssl_verification(True)

            return True
        except ObjectDoesNotExist as e:
            print(e)
            return False

    def accreditation2(self) -> bool:
        authenticator = CloudPakForDataAuthenticator(
            'mmaccaferri',
            '1234567890',
            'https://10.199.44.5:port'
        )

        assistant = AssistantV2(
            version=self.credentials["assistent_version"],
            authenticator=authenticator
        )

        assistant.set_service_url(self.credentials["assistent_url"])