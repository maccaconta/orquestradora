import requests
from decouple import config
import datetime as dt
from api.utilities import fetch, fetchAuthorization


class Middle():
    """"
            Nome            : Middle
            Classe          : Middle
            Criada          : junho-2021
            Descrição       : faz...
    ____________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        self.method = None

    async def async_router(self, attendanceChain_,id_attendance_) -> str:

        """
        ----------------------------------------------------
                Nome            : async_router
                Parametros      : attendance: Orchestrator
                Criada          : junho-2021
                Descrição       : Consome assincronamente serviços da camada middelware
                Retornos        : bool
        ----------------------------------------------------

        """

        retries_: object
        adapter_: object
        session_: requests.Session
        data_: dict
        utl_: str

        #
        # Inicia fluxo de autorização, solicitando o token para os serviços de autorização
        # -------------------------------------------------------

        print(f"[ {dt.datetime.now()}]  *** BUSCANDO TOKEN PRODESP ")

        attendanceChain_[id_attendance_].routers["service"] = await self.authorizationServicesProdesp(attendanceChain_[id_attendance_])

        print(f"[ {dt.datetime.now()}]  *** CREDENCIAIS PRODESP OK:", attendanceChain_[id_attendance_].routers["service"])

        if attendanceChain_[id_attendance_].routers["service"] == {}:
            print(config('ERRO_SERVIDOR_AUTH_PRODESP'))
            return ""

        url_ = config('ORCHEST_URL_HOST') + attendanceChain_[id_attendance_].routers["url"]

        data_ = {
            'service': attendanceChain_[id_attendance_].routers["service"],
            'context': attendanceChain_[id_attendance_].context,
            'parameters': attendanceChain_[id_attendance_].routers["parameters"],
            'id_attendance': id_attendance_
        }

        print(f"[ {dt.datetime.now()}] *** CHAMANDO PROC {url_} PARâMETROS: ", data_)

        # realiza a requsição da proc

        retorno_ = await fetch(url_, data_)

        # verifica a integridade da requisição

        if retorno_["id_attendance"] != id_attendance_:
            print(f"[ {dt.datetime.now()}] ### ALERTA de INTEGRIDADE PROC->ORCHEST: id_attendance_ = ENVIADO: {id_attendance_} - RECEBIDO: {retorno_['id_attendance']}")
            # id_attendance_ = attendanceChain_[retorno_["id_attendance"]]
            return ""

        proc_ = attendanceChain_[id_attendance_].routers['process']

        attendanceChain_[id_attendance_].routers["is_process"] = False
        attendanceChain_[id_attendance_].routers['process'] = ""

        print(f"[ {dt.datetime.now()}]  *** RETORNO DA PROC {proc_}, VARIÁVEIS DE CONTEXTO :", retorno_)

        if retorno_ == {}:
            return ""
        else:
            attendanceChain_[id_attendance_].message["middle"] = retorno_["text"]

            if type(retorno_["context"]) is dict:
                attendanceChain_[id_attendance_].data_service.update(retorno_["context"])
                return id_attendance_

            else:
                print(config('ERRO_VAR_CONTEXTO').format(proc_, retorno_["context"]))
                return ""
    #
    # Obtem token dos servidores de autorização
    # -----------------------------------------

    async def authorizationServicesProdesp(self, attendance):

        service_ = await attendance.getAsyncService(attendance.routers["service"])
        if service_ == {}:
            print(config('ERRO_SEM_SERVICO_CADASTRADO'))
            return ""

        if service_["url_auth"] == "":

            return {
                'token': "",
                'url': service_["url_serv"],
                'canal': '',
                'username': service_["client_id"],
                'password': service_["client_secret"]
            }

        else:
            token_ = await fetchAuthorization(service_["url_auth"], service_)

            try:
                if token_["error"] == 'invalid_scope':
                    token_ ={}
            except:
                pass

            if token_ == {}:
                print(config('ERRO_SERVIDOR_AUTH_PRODESP'), token_)
                return {}

            try:

                return {
                    'token': token_.get("access_token"),
                    'url': service_["url_serv"],
                    'canal': 'portal',
                    'username': "",
                    'password': ""
                }

            except:
                print(config('ERRO_TOKEN_NAO_GERADO'))
                return {}

    #
    #  Recebe os documentos eniados pelo cidadão
    # -----------------------------------------

    def document(self, attendance, file_) -> bool:
        """
        nome: document
        :param attendance: routers
        :param file_: Any
        :return: True, False
        """
        """
                Nome            : document
                Parametro_1     : attendance: Orchestrator
                Parametro_2     : file_
                Criada          : junho-2021
                Descrição       : armazena documentos enviados pelo cidadão
                Retornos        : bool: True, False
        ____________________________________________________________________________________________________
        Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
        """

        _recipient: dict
        _recipient = attendance.routers
        _recipient.update(attendance.citizen)

        if not attendance.saveDocument(attendance.id, _recipient, file_):
            return False
        else:
            return True

