from apscheduler.schedulers.background import BackgroundScheduler
from decouple import config
import requests
import datetime as dt


def startJobs():
    scheduler = BackgroundScheduler()

    scheduler.add_job(task_removeAttendance, 'interval', minutes=int(config('TEMPO_TASK_SCHEDULER_ATT')))
    scheduler.add_job(task_removeWhats, 'interval', minutes=int(config('TEMPO_TASK_SCHEDULER_WHATS')))

    scheduler.start()


def task_removeAttendance():

    url_: str = config('ORCHEST_URL_HOST') + "/orchest/v1/remove/"

    session = requests.Session()
    session.auth = (config('USR_ADMIN_ORCHEST'), config('PWD_ADMIN_ORCHEST'))

    try:
        response_ = session.get(url_)
        print(f"[ {dt.datetime.now()}] --> Execução tarefa de exclusão ok")

    except Exception as e:
        print(f"[ {dt.datetime.now()}] --> Atenção: Retorno da API de exclusão retornou com erro: ", e)

    print("{}".format("-" * 100))


def task_removeWhats():

    url_: str = config('ORCHEST_URL_HOST') + "/orchest/v1/broadcast/removeWhats/"

    session = requests.Session()
    session.auth = (config('USR_ADMIN_ORCHEST'), config('PWD_ADMIN_ORCHEST'))

    try:
        response_ = session.get(url_)
        print(f"[ {dt.datetime.now()}] --> Execução tarefa de exclusão ok")

    except Exception as e:
        print(f"[ {dt.datetime.now()}] --> Atenção: Retorno da API de exclusão WhatsApp retornou com erro: ", e)

    print("{}".format("-" * 100))


def start():

    try:
        startJobs()
        return True

    except:
        return False