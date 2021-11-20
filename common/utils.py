from api.models import Service
from asgiref.sync import sync_to_async
from django.core.mail import EmailMultiAlternatives, message
import sys
import re
from datetime import date, datetime
from base64 import b64decode
import io as BytesIO
from django.conf import settings
from itertools import chain


def func_name_with_err(text: str):
    return f'{sys._getframe().f_back.f_code.co_name}() method error: {text}'


def assembly(datas: dict):
    for data in datas:
        datas[str(data)] = str(datas[str(data)])


async def search_url(service: str):
    data = await sync_to_async(Service.objects.get)(service=service)
    return data


def send_email(configs: dict, document_base64: str):
    repository_ = settings.REPOSITORY
    try:
        citizen_name = f'Prezado(a) {configs["name"]}, \n\n'
        text_template = open(f'{repository_}email_template.html', 'r')

        message = f'{citizen_name}{text_template.read()}'
        subject = configs['subject']
        email_from = configs['sender']
        email_to = configs['receiver']

        document = base64_to_pdf(document_base64)
        
        msg = EmailMultiAlternatives(subject, message, email_from, [email_to])
        msg.attach('Certidao-Negativa-de-Debitos.pdf', document, "application/pdf")
        msg.send()

        return True
    except Exception as e:
        raise Exception(func_name_with_err(e))


def data_validator(entrada: str):
    # print(f'Entrada: {entrada}')
    try:
        date_time_obj = datetime.strptime(entrada, '%d/%m/%Y')
        print(f'# Validador de datas : {date_time_obj.strftime("%d/%m/%Y")}')
        return True
    except Exception as e:
        print('Data inválida')
        print(e)
        return False


def date_parser_formatter(texto: str) -> str:
    res = re.search(r'\b(\d{1,2})[\/\-]*(\d{1,2})[\/\-]*(\d{2}(?:\d{2})?)\b', texto)

    if res:
        dia, mes, ano = res.groups()
        hoje = date.today()
        anoAtual = str(hoje.year)[-2:]
        if mes == 0:
            return False
            
        if len(dia) == 1:
            dia = "0" + dia

        if len(mes) == 1:
            mes = "0" + mes
        
        if len(ano) == 4:
            dtForm = f'{dia}/{mes}/{ano}'
        else:
            preAno = '19' if ano > anoAtual else '20'
            dtForm = f'{dia}/{mes}/{preAno}{ano}'
    
        # print(f'dtForm: {dtForm}')
        if data_validator(dtForm):
            return dtForm
        else:
            return False
    else:
        return False

def phone_parser_formatter(input: str) -> str:
    res = re.search(r'\b[\(0]*([0-9]{2})[\)\s]*([9]*)[\s]*([0-9]{4})[\-\s]*([0-9]{4})\b', input)

    if res:
        area_code, mobile_prefix, phone_part_1, phone_part_2 = res.groups()

        # print(f'area_code: {area_code}, mobile_prefix {mobile_prefix}, phone_part_1 {phone_part_1}, phone_part_2 {phone_part_2}')
        return f'{area_code}{mobile_prefix}{phone_part_1}{phone_part_2}'
    else:
        return False

def base64_to_pdf(base64_):
    try:
        buffer = BytesIO.BytesIO()
        content = b64decode(base64_)
        buffer.write(content)

        return buffer.getvalue()

    except Exception as e:
        raise Exception(func_name_with_err(e))


def search_pdf(pdf_name: str):
    try:
        file = open(f'media/{pdf_name}', 'rb')
        return file.read()
    except Exception as e:
        raise Exception(func_name_with_err(e))


class ValidadorCpf(object):

    def __validarCpf(self, arg):  # type: (CPF) -> bool
        return self.__validarStr(arg.rawValue)

    def __validarStr(self, arg):  # type: (str) -> bool

        if arg == None:
            return False

        p = re.compile('[^0-9]')
        x = p.sub('', arg)

        if len(x) != 11 or len(set(x)) == 1: return False

        return all(self.__hashdigit(x, i + 10) == int(v) for i, v in enumerate(x[9:]))


    def __hashdigit(self, cpf, position):  # type: (str, int) -> int
        """
        Will compute the given `position` checksum digit for the `cpf` input. The input needs to contain all
        elements previous to `position` else computation will yield the wrong result.
        """

        val = sum(int(digit) * weight for digit, weight in zip(cpf, range(position, 1, -1))) % 11

        return 0 if val < 2 else 11 - val

    @staticmethod
    def validar(arg):  # type: (CPF) -> bool or  type: (str) -> bool
        v = ValidadorCpf()

        if type(arg) == CPF: return v.__validarCpf(arg)

        if type(arg) == str: return v.__validarStr(arg)

        return False

def hashdigit(cpf, position):  # type: (str, int) -> int
    """
    Will compute the given `position` checksum digit for the `cpf` input. The input needs to contain all
    elements previous to `position` else computation will yield the wrong result.
    """

    val = sum(int(digit) * weight for digit, weight in zip(cpf, range(position, 1, -1))) % 11

    return 0 if val < 2 else 11 - val

def validarStr(arg):  # type: (str) -> bool

        if arg == None:
            return False

        p = re.compile('[^0-9]')
        x = p.sub('', arg)

        if len(x) != 11 or len(set(x)) == 1: return False

        return all(self.__hashdigit(x, i + 10) == int(v) for i, v in enumerate(x[9:]))


def mascara_email(email: str) -> str:

    indice = int(email.rindex('@')) - 4
    email_tratado = email.replace(email[0: indice], "******")
    return email_tratado


def mascara_telefone(telefone: str) -> str:

    telefone_tratado = telefone.replace(telefone[0: -4], "(XX)XXXXX-")
    return telefone_tratado


def Formatted(variable):
    pattern = re.compile("[\.\-\/\(\) ]", re.IGNORECASE)
    formatted = pattern.sub('', variable)
    return formatted

