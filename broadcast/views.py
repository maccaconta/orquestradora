from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.utilities import run_async
from broadcast.whatsapp.whatsapp import Whatsapp
from decouple import config
import datetime as dt
import time
global chain_phone_

chain_phone_: dict = {}


class ApiWebHooksWhatsapp(APIView):
    """
      Orchest versão 2.0.
      método     : post
      parametros :
      url        : /broadcast/whats
      criado     : junho-2021
      -------------------------------------------
      Todos direitos reservados à Magna Sistemas   (▀̿̿Ĺ̯̿▀̿ ̿)

        Webhook para integração com Whatsapp, a rota dessa API
          deverá ser previamente cadastrada no POSITOS API para comunicação com
           Whatsapp Businness
    """

    permission_classes = [AllowAny]

    @staticmethod
    def post(request):

        data_ = request.data

        if "contacts" in data_:
            whats_: dict = {}

            if not data_.get("messages")[0].get("from") in chain_phone_:
                whats_ = chain_phone_[data_.get("messages")[0].get("from")] = Whatsapp()
            else:

                try:
                    whats_ = chain_phone_[data_.get("messages")[0].get("from")]
                except:
                    whats_ = chain_phone_[data_.get("messages")[0].get("from")] = Whatsapp()

            if whats_.comparing(data_):
                if whats_.setWhats(data_):

                    run_async(chain_phone_[data_.get("messages")[0].get("from")].main)

                    if whats_.encerrar:
                        #chain_phone_[data_.get("messages")[0].get("from")].delete()
                        pass

        return Response({}, status=status.HTTP_200_OK)


class ApiLogado(APIView):
    """
      Orchest versão 2.0.
      método     : post
      parametros :
      url        : /broadcast/ApiLogado/
      criado     : junho-2021
      -------------------------------------------

    """

    permission_classes = [AllowAny]

    @staticmethod
    def post(request, data_):
        data_ = request.data
        response_ = {}

        id_ = data_.get("id", "")

        if id_ == "":

            print("Erro loginSP: Não retornou o telefone para identificar a sessão no Watson")

            response_ = {
                'id': "",
                'status': 'Sem id'
            }

            whats_ = chain_phone_[data_.get("messages")[0].get("from")] = Whatsapp()
            run_async(whats_.main)

        else:

            try:
                whats_ = chain_phone_["+" + id_] = Whatsapp()
                print("Logado : ", chain_phone_[id_])

                run_async(whats_.retornoLoginSP, True)

                response_ = {
                    'id': id_,
                    'status': 'ok'
                }

            except:

                whats_ = chain_phone_[data_.get("messages")[0].get("from")] = Whatsapp()
                run_async(whats_.main)

                response_ = {
                    'id': data_.get("id", ""),
                    'status': 'id não encontrado'
                }

                print("Erro loginSP: Não retornou o telefone para identificar a sessão do Watson")

        return Response(response_, status=status.HTTP_200_OK)


@api_view(('GET',))
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def removeWhats(request):
    agora_ = int(time.time())
    off_: int = 0
    on_: int = 0
    excluidos_ = 0

    agora_ = time.mktime(time.gmtime())

    lst_exclusao_: list = []

    print("{}".format("-" * 100))
    print(f"[ {dt.datetime.now()}] --> Iniciando rotina para exclusão de Whatsapps offline")

    for i, att_ in enumerate(chain_phone_):

        dif_ = agora_ - chain_phone_[att_].timestamp
        duracao_ = time.strftime("%H:%M:%S", time.gmtime(dif_))
        minuto_ = int(time.strftime("%M", time.gmtime(dif_)))

        if minuto_ >= int(config('LIMITE_OFFLINE_WHATS_MIN')):

            if run_async(chain_phone_[att_].encerraWhats):
                lst_exclusao_.append(att_)
                off_ += 1

        else:
            on_ += 1

    if off_ > 0:

        for i in range(off_):
            try:
                print(f"[ {dt.datetime.now()}] --> Excluindo Whatsapps: {lst_exclusao_[i]}")

                lixo_ = chain_phone_.pop(lst_exclusao_[i], None)
                lixo_ = None
                excluidos_ += 1
            except Exception as e:
                print(f"[ {dt.datetime.now()}] --> Erro ao excluir Whatsapps: {lst_exclusao_[i]}", e)

        print("{}".format("-" * 100))
        print(f"[ {dt.datetime.now()}] --> Status: Foram excluídos {excluidos_} Whatsapps")

        return Response({
            'data': dt.datetime.now(),
            'excluidos': excluidos_
        }, status=status.HTTP_201_CREATED)

    else:

        return Response({
            'data': dt.datetime.now(),
            'excluidos': 0
        }, status=status.HTTP_201_CREATED)

