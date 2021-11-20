from api.orchestrator.event_models.event_models import EventModels
from decouple import config
from rx import operators as ops
import datetime as dt
from datetime import datetime
import time
import rx
import uuid


class Orchestrator(Exception,
                   EventModels):

    def __init__(self) -> object:

        self.id_attendance: str
        self.confidance: int
        self.__logged: bool = False  # TODO: implementar metodologia de "deslogar" baseado no tempo do token
        self.session: str
        self.canal: str
        self.user_id: str
        self.created: str
        self.udated: str
        self.success: bool
        self.newAttendance: bool
        self.citizen: dict
        self.message: dict
        self.shipper: dict
        self.context: dict
        self.data_service: dict
        self.process: str
        self.watson: dict
        self.skills: list
        self.nr_skill: int
        self.payload: dict
        self.timestamp: int
        self.nrChamadasApi: int

        self.timestamp = time.mktime(time.gmtime())

        self.id_attendance = ""
        self.created = datetime.now()
        self.confidance = 0
        self.indice = 0
        self.nr_skill = 0
        self.udated = ''
        self.session = ''
        self.user_id = ''
        self.success = False
        self.newAttendance = False
        self.context = {}
        self.data_service = {}
        self.canal = ''
        self.canal_barramento = ''
        self.payload = dict()
        self.nrChamadasApi = 0

        self.routers = {
            'is_documents': False,
            'is_process': False,
            'is_upload': False,
            'is_link': False,
            'is_login': False,
            'is_download': False,
            "url_download": '',
            'process': '',
            'login': '',
            'documents': '',
            'url': '',
            'link': '',
            'service': '',
            'parameters': dict(),
            'fim_chatbot': '',
            'title': '',
            'proc_clean': False
        }

        self.citizen = {
            'id_citizen': '',
            'cpf': '',
            'nickname': '',
            'email': '',
            'mobile': '',
            'client_id': '',
            'full_name': '',
            'ip': '',
        }

        self.message = {
            'intent': '',
            'confidance': 0,
            'question': '',
            'answer': dict(),
            'type_option': '',
            'middle': None
        }

        self.shipper = {
            'longitude': 0,
            'latitude': 0,
        }

        self.data: dict = {
            'type': '',
            'text': '',
            'option': dict(),
            'upload': list(),
            'link': ''}

        self.watson = {
            'source': '',
            'code': '',
            'assistent_apikey': '',
            'assistent_url': '',
            'assistent_version': '',
            'assistent_id': ''}

        self.skills = list()

        #
        # Gera novo id = canal + hash

    def setIdAttendance(self, channel_) -> str:
        cod_channel_: str = ''
        id_attendance: str = ''

        cod_channel_ = self.getChannel(channel_)
        hash_ = str(uuid.uuid4())   # uuid.uuid3(uuid.NAMESPACE_DNS, "python.org")

        if cod_channel_ == '':
            cod_channel_ = '001'

        self.id_attendance = cod_channel_ + "." + hash_

        return self.id_attendance

    def getIdAttendance(self) -> str:
        """
            name: getIdAttendance
            :return: str
        """
        return self.id_attendance

    #
    # Inicializa atendimento
    #

    def setAttendanceRequest(self, shipper: dict, file=None) -> bool:
        """
            name: updateRequest
           :param shipper: dict
           :param file: None
           :return: bool
        """

        try:

            self.session = shipper.get('session', '')
            self.success = True
            self.message["question"] = shipper.get('question', '')
            self.shipper['longitude'] = shipper.get('longitude', 0)
            self.shipper['latidude'] = shipper.get('latitude', 0)
            self.canal = shipper.get('canal', '')
            self.nrChamadasApi += 1

            self.payload = shipper.get('payload', {})

            if self.message["question"] == "LOGIN_SUCESSO":
                self.set_logged()

                self.data_service = self.payload
                self.data_service["loggin"] = ""

            self.data_service["is_logged"] = self.is_logged()

            return True

        except:
            return False

    #
    # Altera o valor do atributo 'loged' para True
    # quando o usuário é logado com sucesso
    #

    def set_logged(self) -> None:
        """
            name: set_logged
            :return: True
        """

        self.__logged = self.__logged == False

    #
    # Verifica se o usário está logado
    #

    def is_logged(self) -> bool:
        """
            name: is_logged
            :return: self.__loggerd, expression_list
        """
        return self.__logged

    #
    # Valida parâmetros do post
    #

    @staticmethod
    def checkParametersRequest(shipper: dict) -> bool:
        """
            Name: checkRequest
            :param shipper: dict
            :return: bool
        """

        # todo: Implementar metodo puxando de um model
        # todo: verificação de tipo
        # todo: fazer verificação do tipo de dado com serializer, olha mais tarde?

        parameters_ = ['id_attendance', 'question', 'session', 'longitude', 'latitude', 'ip', 'canal', 'payload']
        ret_: bool = True

        # verifica a presença de todos os campos
        for key in parameters_:
            if key not in shipper:
                ret_ = False
                break

        return ret_

    def setAuthorization(self, login_data) -> None:

        """
            name: attendanceUpdateAuthData
            :param login_data: login_data
            :return: None
        """
        self.citizen['client_id'] = login_data.get('client_id')
        self.citizen['client_full_name'] = login_data.get('client_full_name')
        self.citizen['client_email'] = login_data.get('client_email')
        self.citizen['client_token'] = login_data.get('client_token')
        self.id_attendance = login_data.get('id_attendance')

    def setAttendance(self, watson_answer: dict) -> None:

        """
            name: attendanceUpdate
            :param watson_answer: watson_answer
            :return: None
        """

        # TODO: Refatorar "Trys"

        param_: dict = {}

        self.udated = datetime.now()
        self.message['answer'] = watson_answer
        self.session = watson_answer['session']

        self.routers['process'] = ''
        self.routers['is_process'] = False

        try:
            param_ = watson_answer["context"]["skills"]['main skill']['user_defined']
        except:
            param_ = {}

        self.context = param_
        self.data_service.update(param_)

        if param_ != {}:

            self.routers['proc_clean'] = True if param_.pop('proc_clean', "False") == "True" else False

            try:
                self.routers['title'] = param_.pop('title', "")
            except:
                self.routers['title'] = ""

            try:
                self.routers['fim_chatbot'] = param_.pop('fim_chatbot', "")
            except:
                self.routers['fim_chatbot'] = ""

            try:
                self.routers['link'] = param_.pop('link', None)
            except:
                self.routers['link'] = ""

            try:
                self.routers['process'] = param_.pop('process', None)

                if self.routers['process'] == "null" or \
                        self.routers['process'] == "" or \
                        self.routers['process'] == "PROC016_ENDPOINT_VANZOLINI":
                    self.routers['process'] = ""

            except:
                self.routers['process'] = ""

            try:
                self.routers['login'] = param_.pop('login', None)
            except:
                self.routers['login'] = ""

            try:
                self.message['type_option'] = param_.pop('type_option', 'menu')
            except:
                self.message['type_option'] = ""

            try:
                self.routers['url_download'] = param_.pop('url_download', None)
            except:
                self.message['url_download'] = ""

            self.routers['parameters'] = param_

            try:
                if self.routers['login'].lower() == 'google' or \
                        self.routers['login'].lower() == 'loginsp':

                    if not self.is_logged():
                        self.routers['is_login'] = True

                else:
                    self.routers['is_login'] = False

            except:
                self.routers['is_login'] = False

            self.routers['is_link'] = True if self.routers['link'] else False

            self.routers['is_download'] = True if self.routers["url_download"] else False

            if self.routers["process"]:
                if self.routers["process"] == "anything_else":
                    self.routers["is_process"] = False
                else:
                    self.routers["is_process"] = True

            try:
                self.routers["documents"] = watson_answer["context"]["skills"]['main skill']['user_defined']['documents']
            except:
                self.routers["documents"] = "[]"

            if self.routers["documents"] == "[]" or \
                    self.routers["documents"] == "":
                self.routers["is_documents"] = False
            else:
                self.routers["is_documents"] = True

    def analyseIntents(self):
        """
            name: analyseIntents
            :return: None
        """
        conf_intents = 0
        conf_entities = 0

        try:
            intents_ = self.message["answer"]["output"].get("intents")

            for int_ in intents_:
                conf_intents = int_["confidence"]
        except:
            conf_intents = 0

        try:
            entities_ = self.message["answer"]["output"].get("entities")
            for ent_ in entities_:
                conf_entities = ent_["confidence"]
        except:
            conf_entities = 0

        rx.of(conf_intents, conf_entities, self.message["confidance"]).pipe(
            self.watsonObserveble()
        ).subscribe(lambda value: self.setConfidance(value))

    def setConfidance(self, value):
        """
            name: setConfidance
            :param value: value
            :return: str
        """
        self.message["confidance"] = value

    @staticmethod
    def watsonObserveble():
        """
            name: watsonObserveble
            :return: rx.pip, expression_list
        """
        return rx.pipe(
            ops.filter(lambda value: value > 0),
        )

    def getCitizenDataLogged(self, data_: dict) -> bool:
        """
            name: getCitizenDataLogged
            :param data_: data_
            :return: bool
        """
        try:
            self.citizen['ip'] = data_.get('ip')
            self.citizen['client_id'] = data_.get('client_id')
            self.citizen['client_full_name'] = data_.get('client_full_name')
            self.citizen['email'] = data_.get('client_email')
            self.citizen['client_token'] = data_.get('client_token')
            return True
        except:
            return False

    def setWatsonCredentials(self, step: int) -> bool:
        """
            name: setWatsonCredentials
            :return: bool
       """

        try:
            self.watson = self.skills[step]
            return True

        except:
            return False

    def getWatsonCredentials(self, canal: str) -> bool:

        self.skills = self.getSkill(canal)

        if not self.skills:
            return False
        else:
            return True

    def getConfidance(self, watson_):

        intents_ = watson_.answer["output"].get("intents")

        try:

            if not intents_:
                return False
            else:

                for int_ in intents_:
                    self.confidance = int_.get('confidence', 0)
                    print("** INTENÇÃO {} >>>>>  CONFIANÇA {} ".format(int_.get('intent'), int_.get('confidence', 0)))
                if len(intents_) > 0:
                    self.confidance = intents_[0].get('confidence')
                    print(
                        f"[ {datetime.datetime.now()}] *** INTENÇÃO {intents_[0].get('intent')} >>>>>  CONFIANÇA {self.confidance} ")
                # for int_ in intents_:
                #     self.confidance = int_.get('confidence', 0)
                #     print(f"[ {datetime.datetime.now()}] *** INTENÇÃO {int_.get('intent')} >>>>>  CONFIANÇA {int_.get('confidence', 0)} ")

                return True
        except:
            return False

    def PreparaDadosRetornoOrchest(self) -> bool:

        """
            name: watsonAnalyser
            :return: bool
        """

        text_: str = ""
        new_skill_: str = ''
        ordem__: list
        data_ = []

        try:

            genericss_ = self.message["answer"]["output"].get("generic")

            for generic_ in genericss_:

                if generic_.get('response_type') == 'text':
                    type_ = 'text'

                    try:

                        if generic_.get('text') is None or generic_.get('text') == '':
                            pass
                        else:

                            if not self.routers['is_link'] and \
                                    not self.routers['is_download']:

                                if generic_.get('text') != "":
                                    data_.append({
                                        'type': "text",
                                        'text': generic_.get('text') + "\n",
                                        'option': {},
                                        'upload': [],
                                        'origem': 'watson',
                                        'link': "",
                                        'title': "",
                                        'ordem': 1
                                    })

                            else:
                                if self.routers['is_link']:

                                    if self.canal == 'whatsapp':
                                        data_.append({
                                            'type': "text",
                                            'text': generic_.get('text') + "\n",
                                            'option': {},
                                            'upload': [],
                                            'origem': 'watson',
                                            'link': "",
                                            'title': "",
                                            'ordem': 1
                                        })

                                        data_.append({
                                            'type': "link",
                                            'text': "",
                                            'option': {},
                                            'upload': [],
                                            'origem': 'watson',
                                            'link': self.routers['link'],
                                            'title': self.routers['title'],
                                            'ordem': 2
                                        })
                                    else:

                                        data_.append({
                                            'type': "link",
                                            'text': generic_.get('text'),
                                            'option': {},
                                            'upload': [],
                                            'origem': 'watson',
                                            'link': self.routers['link'],
                                            'title': self.routers['title'],
                                            'ordem': 2
                                        })

                            text_ += " " + generic_.get('text')

                    except:
                        pass

                if generic_.get('response_type') == 'option':

                    try:
                        if self.message.get('type_option') == "":
                            type_option_ = 'menu_principal'
                        else:
                            type_option_ = self.message.get('type_option')
                    except:
                        type_option_ = 'menu'

                    if self.canal == 'whatsapp':
                        if len(generic_["title"]) > 20:

                            texto_ = generic_["title"]

                            data_.append({
                                'type': "text",
                                'text': texto_,
                                'option': {},
                                'upload': [],
                                'origem': 'watson',
                                'link': "",
                                'title': "",
                                'ordem': 5.9
                            })

                            generic_["title"] = "Escolha sua opção:"

                            option_ = {
                                'select': generic_,
                                'type_option': type_option_
                            }

                            data_.append({
                                'type': "option",
                                'text': "",
                                'option': option_,
                                'upload': [],
                                'origem': 'watson',
                                'link': "",
                                'title': "",
                                'ordem': 6
                            })

                    else:

                        option_ = {
                            'select': generic_,
                            'type_option': type_option_
                        }

                        data_.append({
                            'type': "option",
                            'text': "",
                            'option': option_,
                            'upload': [],
                            'origem': 'watson',
                            'link': "",
                            'title': "",
                            'ordem': 6
                        })

                if generic_.get('response_type') == 'suggestion':
                    option_ = {
                        'select': {'options': generic_["suggestions"]},
                        'type_option': self.message.get('type_option', 'menu')
                    }

                    data_.append({
                        'type': "option",
                        'text': "",
                        'option': option_,
                        'upload': [],
                        'origem': 'watson',
                        'link': "",
                        'title': "",
                        'ordem': 6

                    })

            if self.routers['is_documents']:
                data_.append({
                    'type': "upload",
                    'text': "",
                    'option': {},
                    'upload': self.routers['documents'].split(","),
                    'origem': 'watson',
                    'link': "",
                    'title': "",
                    'ordem': 4
                })

            if self.routers['is_login']:
                data_.append({
                    'type': "login",
                    'text': "",
                    'option': {},
                    'upload': [],
                    'origem': 'watson',
                    'link': self.routers['link'],
                    'title': text_,
                    'ordem': 5
                })

            if self.routers['is_download']:
                data_.append({
                    'type': "download",
                    'text': "",
                    'option': {},
                    'upload': [],
                    'origem': 'watson',
                    'link': self.routers["url_download"],
                    'title': text_,
                    'ordem': 3
                })

            data_ordenado_ = []
            data_ordenado_ = sorted(data_, key=lambda o: o['ordem'])

            if self.routers['process'] == "anything_else":
                new_skill_ = config('ASSISTANT_ANYTHING_URL')

            self.data = {
                'data': data_ordenado_,
                'anythingelseURL': new_skill_,
                'fim_chatbot': self.routers['fim_chatbot']
            }

        except:
            self.data = dict(type="erro", text='', option={}, upload=[], link="")
            return_ = False

        self.analyseIntents()

        return True
