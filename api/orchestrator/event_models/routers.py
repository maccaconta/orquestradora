from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist

from api.models import Routers
from api.serializer import RoutersSerializer
from decouple import config
import datetime as dt

class EventModelRouters:

    @staticmethod
    async def getRouters(router) -> dict:

        """
        :name: getRouters , atualiza as rotas cadastradas no sistema
        :param router:
        :return:router dict
        """
        try:

            print(f"[ {dt.datetime.now()}]  *** GET PROC : ", str(router["process"]).strip())

            get_ = await sync_to_async(Routers.objects.get, thread_sensitive=True)(process=str(router["process"]).strip())

            return RoutersSerializer(get_).data

        except ObjectDoesNotExist:
            print(f"[ {dt.datetime.now()}] *** {router['process']} não cadastrada {config('ERRO_URL_PROC_N_ENCONTRADA')}")
            pass

        return router
