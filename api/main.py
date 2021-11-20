from asgiref.sync import sync_to_async

from api.middle import Middle
from api.watson import Watson
from decouple import config
from common.utils import date_parser_formatter, phone_parser_formatter
import datetime as dt

watson_: Watson = Watson()


async def Main(attendanceChain_, id_attendance_):
    """
    name: Main
    :param attendance_: attendance
    :return: attendance {status}
    """

    retorno_ = id_attendance_

    try:

        ret_ = await fecth_watson(attendanceChain_[id_attendance_])

        attendanceChain_[id_attendance_].setAttendance(watson_.answer)

        while attendanceChain_[id_attendance_].routers["is_process"]:

            print("{}".format("-" * 100))
            print(f"[ {dt.datetime.now()}]  *** BUSCANDO a URL DA PROC NA TABELA ROUTERS", attendanceChain_[id_attendance_].routers["process"])

            _last = attendanceChain_[id_attendance_].routers
            try:
                _router = await attendanceChain_[id_attendance_].getRouters(attendanceChain_[id_attendance_].routers)
            except Exception as e:
                print(f"[ {dt.datetime.now()}]  ###  URL  NÃO ENCONTRADA --> VERIFIQUE A TABELA ROUTERS ou FIX_ROUTERS...", e)
                raise Exception(500)

            attendanceChain_[id_attendance_].routers = dict(_last, **_router)

            id_attendance_retorno_ = await Middle().async_router(attendanceChain_,id_attendance_)

            if id_attendance_retorno_ == "":
                print(config('ERRO_CHAMADA_PROC'))
                raise Exception(500)
            else:

                if id_attendance_retorno_ != id_attendance_:
                    print(f"[ {dt.datetime.now()}]  ### ALERTA de INTEGRIDADE MIDDLE->MAIN: id_attendance_ = ENVIADO: {id_attendance_} - RECEBIDO: {retorno_['id_attendance']}")
                    # id_attendance_ = id_attendance_retorno_
                    raise Exception(500)

                print(f"[ {dt.datetime.now()}]  *** ENVIANDO DADOS DA PROC PARA O WATSON : ", attendanceChain_[id_attendance_].message["middle"], attendanceChain_[id_attendance_].data_service)

                attendanceChain_[id_attendance_].routers["is_process"] = False
                attendanceChain_[id_attendance_].routers["process"] = ""
                attendanceChain_[id_attendance_].data_service["process"] = ""
                attendanceChain_[id_attendance_].data_service["link"] = ""
                attendanceChain_[id_attendance_].data_service["type_option"] = "menu"
                attendanceChain_[id_attendance_].data_service["canal"] = attendanceChain_[id_attendance_].canal

                if not watson_.send(
                        attendanceChain_[id_attendance_].session,
                        attendanceChain_[id_attendance_].message["middle"],
                        attendanceChain_[id_attendance_].data_service):
                    print(config('WATSON_ERROR'))
                    raise Exception(500)
                else:

                    attendanceChain_[id_attendance_].setAttendance(watson_.answer)

                    if attendanceChain_[id_attendance_].routers["is_process"]:
                        continue
                    else:
                        break

        retorno_ = attendanceChain_[id_attendance_].id_attendance

    except Exception as e:
        retorno_ = ""

    return retorno_


async def fecth_watson(attendance_):
    return_: bool = False

    attendance_.setWatsonCredentials(attendance_.nr_skill)

    attendance_.data_service.update(attendance_.context)

    if not watson_.connect(attendance_.watson):
        return False
    else:

        attendance_.data_service["response_type"] = ""
        attendance_.data_service["title"] = ""
        attendance_.data_service["canal"] = attendance_.canal
        attendance_.data_service["process"] = ""
        attendance_.data_service["link"] = ""
        attendance_.data_service["type_option"] = "menu"

        if "question" in attendance_.message:
            aux = date_parser_formatter(attendance_.message['question'])
            if aux:
                attendance_.data_service["found_date"] = aux
            else:
                attendance_.data_service["found_date"] = None

            aux = phone_parser_formatter(attendance_.message['question'])
            if aux:
                attendance_.data_service["found_phone"] = aux
            else:
                attendance_.data_service["found_phone"] = None

        if attendance_.routers["proc_clean"]:
            attendance_.routers["proc_clean"] = False

            new_params_ = {}

            for key in attendance_.data_service:
                new_params_[key] = None

            attendance_.data_service = new_params_

            print(" executando proc clean")

        if not watson_.send(
                attendance_.session,
                attendance_.message['question'],
                attendance_.data_service):
            print(config('WATSON_ERROR'))
            return False

        # else:

        #     # print(f'&*&*&*&*&*&*&*&&*&*&*&*&*   {watson_.answer["output"]}')
        #     if not attendance_.getConfidance(watson_):
        #         return True

        #     else:

        #         #
        #         # Caso o grau de confiança da intenção seja menor que o parãmetro
        #         #  ASSISTANT_MIN, o fluxo é desviado para a itenção ASSISTANT_DEFAULT
        #         #  definidos no arquivo .env
        #         # --------------------------------------------------------------

        #         if attendance_.confidance < (float(config('ASSISTANT_MIN')) / 100):

        #             attendance_.data_service["last_input"] = attendance_.message["question"]

        #             print(f"[ {dt.datetime.now()}] *** GRAU DE CONFIANÇA : {attendance_.confidance} - LIMITE CONFIGURADO : {float(config('ASSISTANT_MIN')) / 100}")
        #             print(f"[ {dt.datetime.now()}] *** ORCHEST ENVIANDO REQUSIÇÃO PARA DISCOVERY : ", attendance_.data_service["last_input"])

        #             if not watson_.send(
        #                     attendance_.session,
        #                     config('ASSISTANT_DEFAULT'),
        #                     attendance_.data_service):
        #                 print(config('WATSON_ERROR'))
        #                 return False

        #             # attendance_.setAttendance(watson_.answer)
        #             print(f"[ {dt.datetime.now()}] *** WATSON RESPONSE DISCOVERY : ", watson_.answer)

        #     return True
