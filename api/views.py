from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.main import Main
from api.utilities import run_async
from api.orchestrator.orchest import Orchestrator
from decouple import config
from django.http import JsonResponse
from django.shortcuts import render
import datetime as dt
import json
import time

global attendanceChain_

attendanceChain_: dict = {}


class ApiOrchest(APIView):
    """
    _________________________________________________________________________________________
    Orchest versão 2.0.
    método     : post
    parâmetros : ['id_attendance', 'question', 'session', 'longitude', 'latitude', 'ip', 'canal', 'payload']
    url        : /orchest/v1/watson
    criada     : maio-2021
    _________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)

             A API Orchest v.2 é um serviço de atendimento por chabot que utiliza a tecnologia de inteligência
        artificial do IBM Watson Assistant para orientar os cidadãos na resolução de  problemas relativos aos
        serviços digitais do Detran.

             A API Orchest v.2 foi desenvolvida com tecnologia Python Django Framework Rest 3.12.4

             A API Orchest identifica a intenção do atendimento, orienta o fluxo de conversação e encaminha o cidadão
        para o serviço do Detran mais adequado para a solução do problema.

             A API Orchest também  estabelece comunicação com os serviços de mensageria públicas Whatsapp, Telegram
        e Mensager.
    _________________________________________________________________________________________

         Orhest é dividido em 4 camadas:

        - Orchest, responsabilidades:
            a) Orquestração entre o chatbot e o Watson.
            b) Inicia, gerencia e encerra os atendimentos.
            c) Estabelece comunicação entre orquestradora e demais módulos (Middle, Broadcast)

        - Watson, persiste a comunicação com o IBM Assistant
            b) Abre e apaga sessões
            c) Envia e recebe mensagens do Watson
            d) Atualiza variáveis de contextos

        - Middle, responsabilidades:
            a) Processos e regras de negócio da PRODESP
            b) Consumo de serviços do Detran e Poupatempo

        - Broadcast
            a) realiza a comunicação com as plataformas de mensageria (Whatsapp etc.)

    _________________________________________________________________________________________

    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request):
        id_attendance_: str = ""
        attendance_: Orchestrator = Orchestrator()
        shipper_ = request.data

        print(f"[ {dt.datetime.now()}]  *** ORCHEST REQUEST ", shipper_)

        try:

            # Valida parâmetros recebidos pela view
            # -------------------------------------

            if not attendance_.checkParametersRequest(shipper_):
                raise Exception(400)

            if str(shipper_.get('id_attendance')) != "0" and \
                    str(shipper_.get('id_attendance')) != "":
                id_attendance_ = str(shipper_.get('id_attendance'))

            # Caso id_attendance_ for vazio, cria um novo atendimento
            # ----------------------------------------------------

            if id_attendance_ == "":

                id_attendance_ = attendance_.setIdAttendance(shipper_.get('canal'))

                if id_attendance_ == "":
                    print(config('ERRO_CRIACAO_ID'))
                    raise Exception(500)

                if not attendance_.getWatsonCredentials(shipper_.get('canal')):
                    print(config('ERRO_CREDENCIAIS_WATSON'))
                    raise Exception(500)

                #
                # Inclui um atendimento na lista de atendimentos
                # ----------------------------------------------

                attendanceChain_[id_attendance_] = attendance_

            else:
                try:

                    # Recupera atendimento e atualiza o timestamp

                    attendanceChain_[id_attendance_].timestamp = time.mktime(time.gmtime())

                except:

                    # Cria um novo atendimento caso o id do atendimento tenha sido excluido
                    # Todo, verificar a possibiidade de retomar o atendimento.

                    shipper_["question"] = ""
                    shipper_["session"] = ""

                    id_attendance_ = attendance_.setIdAttendance(shipper_.get('canal'))

                    if id_attendance_ == "":
                        print(config('ERRO_CRIACAO_ID'))
                        raise Exception(500)

                    if not attendance_.getWatsonCredentials(shipper_.get('canal')):
                        print(config('ERRO_CREDENCIAIS_WATSON'))
                        raise Exception(500)

                    attendanceChain_[id_attendance_] = attendance_

            if not attendanceChain_[id_attendance_].setAttendanceRequest(shipper_):
                print(config('ERRO_PARAMETROS_API'))
                raise Exception(400)

            # Executa a função Main na thread principal ou
            # abre uma nova thread no pool de threads para executá-la
            # run_async aceita apenas o tipo tupla como parâmetro
            # --------------------------------------------------------

            id_attendance_ = run_async(Main, attendanceChain_, id_attendance_, )

            if id_attendance_ != "":

                if attendanceChain_[id_attendance_].PreparaDadosRetornoOrchest():

                    data_retorno_ = attendanceChain_[id_attendance_].data
                    session_ = attendanceChain_[id_attendance_].session
                    sucesso_ = True
                    status_ = status.HTTP_201_CREATED

                    # Salva Bulck
                    # ------------

                    data_save = {
                        "session": session_,
                        "question": attendanceChain_[id_attendance_].message['question'],
                        "answer": attendanceChain_[id_attendance_].watson
                    }

                    attendanceChain_[id_attendance_].saveBulk(data_save)

                else:
                    print(config('ERRO_CRIACAO_DADOS_RETORNO'))
                    raise Exception(500)

            else:

                raise Exception(500)

        except json.decoder.JSONDecodeError as e:
            print(config('ORCHEST_MSG_ERRO_PARAMETROS_API'), e)
            status_ = status.HTTP_400_BAD_REQUEST
            data_retorno_ = {}
            session_ = ""
            id_attendance_ = 0
            sucesso_ = False

        except Exception as e:
            print(config('MSG_ERROR'), e)
            status_ = status.HTTP_500_INTERNAL_SERVER_ERROR
            session_ = ""
            id_attendance_ = 0
            data_retorno_ = {}
            sucesso_ = False

        return_ = {'success': sucesso_,
                   'id_attendance': id_attendance_,
                   'watson': data_retorno_,
                   'session': session_}

        print(f"[ {dt.datetime.now()}]  *** ORCHEST API RESPONSE : {id_attendance_}  {data_retorno_}")

        return Response(return_,
                        status=status_,
                        template_name=None,
                        headers=None,
                        content_type="application/json")


@api_view(['GET'])
@permission_classes([AllowAny])
def monitorAttendance(request):
    agora_ = int(time.time())
    off_: int = 0
    on_: int = 0
    nrChamadas_: int = 0
    totalChamadas_: int = 0
    TotalAtendimentos_: int = 0
    mediaChamadas_: float = 0.0
    nrChamadasON_: int = 0
    mediaChamadasON_: float = 0.0
    data_retorno_: dict = {}
    lst_retorno_: list = []

    agora_ = time.mktime(time.gmtime())

    print(f" [ {dt.datetime.now()}]")
    print(" {}".format("-" * 95))
    print(" {:>10}  {:>25}  {:>25}  {:>13}  {:>9}".format("Status", "Atendimento", "Cronômetro",  "Atualização", "Chamadas"))
    print(" {}".format("-" * 95))

    for i, att_ in enumerate(attendanceChain_):

        dif_ = agora_ - attendanceChain_[att_].timestamp
        duracao_ = time.strftime("%H:%M:%S", time.gmtime(dif_))
        minuto_ = int(time.strftime("%M", time.gmtime(dif_)))

        nrChamadas_ = attendanceChain_[att_].nrChamadasApi
        totalChamadas_ += nrChamadas_

        if minuto_ >= int(config('LIMITE_OFFLINE_ATT_MIN')):
            off_ += 1
            status_ = "off"

        else:
            on_ += 1
            nrChamadasON_ += nrChamadas_
            status_ = "on "

        lst_retorno_.append({
            'id_attendance': att_,
            'created': attendanceChain_[att_].created,
            'canal': attendanceChain_[att_].canal,
            'duracao': duracao_
        })

        _udated = attendanceChain_[att_].udated.strftime("%H:%M:%S")

        print("{:>10}  {:>40}  {:>10}  {:>13}  {:>6}".format(status_, att_, duracao_, _udated, nrChamadas_))

    totalAtendimentos_ = len(attendanceChain_)

    if totalAtendimentos_ > 0:
        mediaChamadas_ = round(totalChamadas_ / totalAtendimentos_, 2)
    else:
        mediaChamadas_ = 0

    if on_ > 0:
        mediaChamadasON_ = round(nrChamadasON_ / on_)
    else:
        mediaChamadasON_ = 0

    print(" {}".format("-" * 95))
    print(" {:>46} {:>30}".format("Chamadas", "Chamadas Orchest"))
    print(" {:>20} {:>11}  {:>11}  {:>20} {:>10}".format("online", "ofline", "x̄ on", "total", "x̄"))
    print(" {}".format("-" * 95))
    print(" {:>20} {:>10}  {:>10}  {:>20} {:>10}".format(on_, off_, mediaChamadasON_, totalChamadas_, mediaChamadas_))

    return Response({
        'data': dt.datetime.now(),
        'online': on_,
        'offline': off_,
        'atendimentos': lst_retorno_
    }, status=status.HTTP_201_CREATED)


@api_view(('GET',))
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def removeAttendance(request):
    agora_ = int(time.time())
    off_: int = 0
    on_: int = 0
    excluidos_ = 0

    agora_ = time.mktime(time.gmtime())

    lst_exclusao_: list = []

    print(f" [ {dt.datetime.now()}]")
    print(" {}".format("-" * 100))
    print(" {:>10}  {:>25}  {:>25}  {:>13}  {:>9}".format("Status", "Atendimento", "Cronômetro", "Atualização","Chamadas"))
    print(" {}".format("-" * 100))

    for i, att_ in enumerate(attendanceChain_):

        dif_ = agora_ - attendanceChain_[att_].timestamp
        duracao_ = time.strftime("%H:%M:%S", time.gmtime(dif_))
        minuto_ = int(time.strftime("%M", time.gmtime(dif_)))

        try:
            udated_ = attendanceChain_[att_].udated.strftime("%H:%M:%S")
        except:
            pass

        nrChamadas_ = attendanceChain_[att_].nrChamadasApi

        if minuto_ >= int(config('LIMITE_OFFLINE_ATT_MIN')):

            lst_exclusao_.append(att_)
            off_ += 1
            status_ = "off "

        else:
            on_ += 1
            status_ = "on "

        print("{:>10}  {:>40}  {:>10}  {:>13}  {:>6}".format(status_, att_, duracao_, udated_, nrChamadas_))

    print(" {}".format("-" * 100))
    print(" {:>20} {:>30}  {:>40}  ".format("online", "ofFline",  "total" ))
    print("{}".format("-" * 100))
    print(" {:>20} {:>30}  {:>40}".format(on_, off_, on_+ off_))
    print("{}".format("-" * 100))

    if off_ > 0:

        print(f"[ {dt.datetime.now()}] --> Iniciando rotina para exclusão de atendimentos offline")

        for i in range(len(lst_exclusao_)):
            try:
                print(f"[ {dt.datetime.now()}] --> Excluindo atendimento: {lst_exclusao_[i]}")
                lixo_ = attendanceChain_.pop(lst_exclusao_[i], None)
                lixo_ = None
                excluidos_ += 1
            except Exception as e:
                print(f"[ {dt.datetime.now()}] --> Erro ao excluir atendimento: {lst_exclusao_[i]}", e)

        print("{}".format("-" * 100))
        print(f"[ {dt.datetime.now()}] --> Status: Foram excluídos {excluidos_} atendimentos")

        return Response({
            'data': dt.datetime.now(),
            'excluidos': excluidos_
        }, status=status.HTTP_201_CREATED)

    else:
        return Response({
            'data': dt.datetime.now(),
            'excluidos': 0
        }, status=status.HTTP_201_CREATED)


def index(request):
    return render(request, 'index.html')


def ApiLoginSP(request):
    args: dict = {}

    if request.method == 'GET':

        try:
            args['id'] = request.GET["id"]

        except:
            args['id'] = ""

        if args['id'] == "":
            print(f"[ {dt.datetime.now()}] --> Erro, identificador do usuário no Whatsapp não fornecido")

    return render(request, "login.html", args)


def ApiLoginSPRedirect(request):
    return render(request, "login.html")


def ApiLoginSPCrentials(request):
    credentials_ = {
        'clientId': config('CLIENT_ID'),
        'responseType': "code",
        'scope': "openid profile",
        'client_secret': config('CLIENT_SECRET'),
        'issuer': config('ISSUER')

    }

    return JsonResponse(credentials_)
