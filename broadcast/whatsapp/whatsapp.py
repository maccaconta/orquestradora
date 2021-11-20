
from api.utilities import fetch, fetchPOST, fetchPOSTproxy
from datetime import datetime
import datetime as dt
from broadcast.whatsapp.whats_templates.whats_templates import WhatsTemplates
from decouple import config
import time

class Whatsapp(WhatsTemplates):

    def __init__(self):

        self.msg_body: str = ""
        self.created_at: int = 0
        self.from_number: str = ""
        self.id_msg: str = ""
        self.id_whatsapp: str = ""
        self.is_upload: bool = False
        self.docs_count: int = 0
        self.encerrar: bool = False
        self.timestamp: int = 0

        self.data_send: dict = {
            'id_attendance': 0,
            'question': "",
            'session': "",
            'longitude': 0,
            'latitude': 0,
            'ip': "",
            'canal': "whatsapp",
            'payload': {},
        }

        self.data_receive: dict = {}

    # ----------
    # Main

    async def main(self):

        """
        ------------------------------------
        name:  main
        Método principal chamado pela webhook cadastrada na Positus
        :param data: data
        :return:
        ------------------------------------
        """

        # Todo: a implementar observanble para repetição de mensagens

        data_return_ = {}

        self.timestamp = time.mktime(time.gmtime())

        if self.docs_count == 0 and self.is_upload:
            self.msg_body = 'upload_ok'

        self.data_send["canal"] = "whatsapp"

        if self.docs_count == 0:
            if not self.eNovoAtendimento(self.msg_body.lower()):

                self.data_send["question"] = self.msg_body

            else:
                self.data_send["question"] = ""
                self.data_send["session"] = ""
                self.data_send["id_attendance"] = 0

            data_return_ = await self.sendOrchestrator()

        else:
            self.msg_body = 'Você tem documentos pendentes ou informe "menu" para voltar a outras opções'

        if data_return_ != {}:

            self.data_receive = data_return_.get("watson")
            data_ = self.data_receive.get("data")

            for obj in data_:

                self.data_send["answer"] = obj["text"]

                data_return_ = await self.sendWhats(obj)

                if "Agradecemos seu contato" in obj["text"]:
                    self.encerrar = True
                    print(f"[ {dt.datetime.now()}] ___5.Encerrando atendimento do whatsapp : ", data_return_.text)

        if self.docs_count == 0 and self.is_upload:
            self.is_upload = False

        return data_return_

    async def encerraWhats(self) -> bool:

        token_ = config('WHATS_TOKEN')
        url_ = config('WHATS_URL')

        headers_ = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(token_)
        }

        try:

            payload_ = {'to': "", 'type': "text", 'text': {'body': ""}}

            payload_['to'] = self.from_number
            payload_['text']['body'] = "Estamos encerrando nosso atendimento por inatividade, quando precisar falar novamente comigo é só digitar a palavra MENU.⭐   "

            data_ = await fetchPOST(url_, payload_, headers_)

            print(f"[ {dt.datetime.now()}] ___ 6.ENCERRANDO ATENDIMENTO WHATSAPP POR INATIVIDADE")

            return True

        except:
            return False

    # ----------
    # setWhats

    def setWhats(self, data: dict) -> bool:
        """
        ------------------------------------
        name: setWhats
        Atualiza os atributos da classe  com informações
            da mensagem do whatsapp
        :param data: data
        :return:
        ------------------------------------
        """

        # Verifica a quantidade de documentos enviadas pela usuário
        # ---------------------------------------------------------

        self.documentsCountDecrement(data)

        text_value_: str = ""

        try:
            if data.get("messages")[0]['type'] == 'text':
                text_value_ = data.get("messages")[0]['text'].get('body')
            elif data.get("messages")[0]['type'] == 'interactive':
                text_value_ = data.get("messages")[0]['interactive']['button_reply'].get('title')
            # elif data.get("messages")[0]['type'] == 'document':
            #     print(data.get("messages")[0]['document']['filename'])

            self.msg_body = text_value_
            self.created_at = datetime.fromtimestamp(int(data.get("messages")[0].get("timestamp")))
            self.from_number = "+" + data.get("messages")[0].get("from")
            self.id_msg = data.get("messages")[0].get("id")
            self.id_whatsapp = data.get("contacts")[0].get("wa_id")

            return True

        except:
            return False

    # ----------------------------------------------------
    # sendOrchestrator

    async def sendOrchestrator(self):

        """
        :sendOrchestrator
         Médodo de envio de uma mensagem para API Oquestradora
        """

        try:

            print(f"[ {dt.datetime.now()}] ___1.BROADCAST PARA ORCHEST : ", self.data_send )

            return_ = await fetch(config('ORCHEST_URL_PUBLIC') + "/orchest/v1/watson/", self.data_send)

            print(f"[ {dt.datetime.now()}] ___2.ORCHEST PARA BRDADCAST : ", return_ )

            self.data_send["session"] = return_.get("session")
            self.data_send["id_attendance"] = return_.get("id_attendance")

            self.data_send["question"] = ""

            return return_

        except Exception as e:
            return {}

    # -----------------------------------------------
    # sendWhats

    async def sendWhats(self, data_receive_):

        """
        ------------------------------------
        sendWhats: Médodo de envio de uma mensagem para o Whatsapp
        :parameter
        ------------------------------------
        """

        token_ = config('WHATS_TOKEN')
        url_ = config('WHATS_URL')
        proxy_ = config('PROXY_WHATS')

        headers_ = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(token_)
        }

        payload_ = await self.templateMount(self.from_number, data_receive_, self.data_send)

        print(f"[ {dt.datetime.now()}] ___3.BROADCAST PARA WHATSAPP : ", payload_)

        data_ = await fetchPOSTproxy(url_, payload_, headers_, proxy_)

        # Verificar se é tipo upload e contar quantidade de documentos
        self.documentsCounting(data_receive_)

        print(f"[ {dt.datetime.now()}] ___4.WHATSAPP PARA BROADCAST : : ", data_)

        return data_

    # ----------------------------------------------------
    # retornoLoginSP

    async def retornoLoginSP(self, status: bool):

        """
        :name: retornoLoginSP
        Médodo de retorno do LoginSP com autenticação validada
        :status: boolean
        """

        if status:
            self.data_send["question"] = "LOGADO"
        else:
            self.data_send["question"] = "NAO_LOGADO"

        data_return_ = await self.sendOrchestrator()

        if data_return_ != {}:
            data_return_ = await self.sendWhats()

    # ----------------------------------------------------
    #  comparing

    def comparing(self, data: dict) -> bool:

        """
        ------------------------------------
        name: comparing
        Compara retornos da Webhook para selecinar somente
        :param data: data
        :return: bool
        ------------------------------------
        """

        try:
            if self.msg_body == data.get('messages')[0]['text'].get('body') and \
                    self.from_number == data.get('messages')[0].get('from'):
                return False

            else:
                return True
        except:
            return True

    def documentsCounting(self, data: dict) -> None:
        """
        ------------------------------------
        name: documentsCounting
        :param data: data
        :return: bool
        ------------------------------------
        """
        if data['type'] == 'upload' and not self.is_upload:  # and self.docs_count > 0
            self.is_upload = True
            self.docs_count = len(data["upload"][0])
            print(f'DOCUMENTO CONTADOR: {self.docs_count}')

    def documentsCountDecrement(self, data: dict) -> None:
        """
        ------------------------------------
        name: documentsCountDecrement
        :param data: data
        :return: bool
        ------------------------------------
        """

        try:
            for msg in data['messages']:
                if msg['type'] == 'document' and self.is_upload:
                    self.docs_count = self.docs_count - 1
        except:
            pass

    def eNovoAtendimento(self, texto):

        palavras_reservadas_ = ["ola",
                                "bom dia",
                                "boa noite",
                                "boa tarde",
                                "beleza",
                                "bl",
                                "tranquilo",
                                'tranquila",'
                                "tudo bem",
                                "como vai",
                                "oi",
                                "fala",
                                "diga",
                                "converse",
                                "me ajuda",
                                "ajuda eu",
                                "ajuda",
                                "help",
                                "socorro",
                                'menu',
                                'menu principal']

        if texto in palavras_reservadas_:
            return True
        else:
            return False
