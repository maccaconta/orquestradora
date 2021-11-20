from django.apps import AppConfig
import os
import json

from Prodesp_Chabot import settings
from decouple import config



class ApiConfig(AppConfig):
    """
             Name           : ApiConfig
            :class          : Class ApiConfig
            :create         : junho-2021
            :param          : AppConfig
            description     : Incializa o arquivo environment.json, utilizado pelo webclient,
                                com variáveis de ambiente.
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas
    """
    name = 'api'

    def ready(self):

        # Criação automática do arquivo enviroment.json,
        # utilizado pelo front Angular.
        # ---------------------------------------------

        name = 'api'

        json_: dict = {
            'title': config('WEBCLIENT_TITLE'),
            'orchest_url_host': config('ORCHEST_URL_HOST'),
            'msg_sem_servico': "Servico nao encontrado ... aguarde um momento, estamos retornando para o ",
            'canal': config('CANAL')
        }

        with open('api' + settings.STATIC_URL + 'environment.json', 'w') as f:
            json.dump(json_, f)

        f.close()

        from api.task import start
        start()

