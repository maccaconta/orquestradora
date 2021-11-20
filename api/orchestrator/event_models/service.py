from asgiref.sync import sync_to_async
from decouple import config
from django.core.exceptions import ObjectDoesNotExist

from api.models import Service
from api.serializer import ServiceSerializer


class EventModelServiceMixin(object):

    async def getAsyncService(self, service: str) -> dict:

        try:

            get_ = await sync_to_async(Service.objects.get)(service=service)

            if not config('SERVICOS_PRODESP_PRODUCAO', cast=bool):

                retorno_ = {
                    'client_secret': get_.client_secret,
                    'client_id': get_.client_id,
                    'grant_type': get_.grant_type,
                    'scope': get_.scope,
                    'url_auth': get_.url_auth_homo,
                    'url_serv': get_.url_serv_homo
                }

            else:
                retorno_ = {
                    'client_secret': get_.client_secret,
                    'client_id': get_.client_id,
                    'grant_type': get_.grant_type,
                    'scope': get_.scope,
                    'url_auth': get_.url_auth_prod,
                    'url_serv': get_.url_serv_prod
                }

            return retorno_

        except:
            return {}



