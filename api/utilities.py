
from requests.adapters import HTTPAdapter
from aiohttp.web_exceptions import HTTPServerError, HTTPError

import threading
from base64 import b64decode
from .models import Channel
from decouple import config

import aiohttp

import asyncio
import uuid
import json
import re
import ast
import os
from datetime import datetime, timedelta, date

from django.conf import settings


def key_generator(channel: str) -> str:
    """
    key_generator: retorna retorna uma chave de identificação baseado na tabela (channel=canal)
    :param channel (whatsapp, webcliente etc)
    :return: id do atendimento
    """

    try:
        data_ = Channel.objects.get(channel=channel)
        data_ = data_.code

        return "{data}.{key}".format(data=data_, key=uuid.uuid3(uuid.NAMESPACE_DNS, "python.org"))
    except:
        return False


# -----------------------------
# Função de chamada assincrona customizadas
# --------------------------------

class RunThread(threading.Thread):
    def __init__(self, func, args, kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None
        super().__init__()

    def run(self):
        self.result = asyncio.run(self.func(*self.args, **self.kwargs))


def run_async(func, *args, **kwargs):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    if loop and loop.is_running():
        thread = RunThread(func, args, kwargs)
        thread.start()
        thread.join()
        return thread.result
    else:
        return asyncio.run(func(*args, **kwargs))


# -----------------------------
# Funções fetchGet + retryGet
# -----------------------------

async def fetchGET(url_, headers_: dict = None) -> dict:
    """
    ----------------------------------------------------
    descrição : Função assincrôna fetchGET método Get
    :param headers_:
    :param url_: str
    :return: json
    ----------------------------------------------------
    """

    retorno_: dict = {}

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    #
    # Tenta 3 vezes a requisição get
    # -------------------------------

    for _ in range(3):

        retorno_ = await retryGET(url_, headers_)

        if retorno_ != {}:
            break

    return retorno_


async def retryGET(url_, headers_) -> dict:
    try:
        async with aiohttp.ClientSession(headers=headers_) as session:

            async with session.get(url=url_) as resp:

                try:
                    # Retorno do tipo JSON
                    return await resp.json()

                except:
                    try:
                        # Retorno do tipo binário
                        data_ = await resp.read()
                        dict_str = data_.decode("UTF-8")
                        return ast.literal_eval(dict_str)

                    except:
                        # Retorno do tipo Text
                        return await resp.text()

    except Exception as e:
        print("Except with get ", e)

        return {'code', e}


async def retryGET_deprecated(url_, headers_: dict = None) -> dict:
    # urlencode({"q":message})
    try:
        async with aiohttp.ClientSession(headers=headers_) as session:

            async with session.get(url_, raise_for_status=True) as resp:
                try:
                    return await resp.json()
                except:
                    return await resp.text()

    except Exception as e:
        print("Except with get ", e)

    return {}

# -----------------------------
# Funções fetchPost + retryPost
# -----------------------------


async def fetchPOST(url_: str, data_: dict, headers_: dict = None) -> dict:
    """
    ----------------------------------------------------
    fetch: Requisita assincronamente por método post
    :param headers_: dict
    :param url_: str
    :param data_: dict
    :return: dict
    ----------------------------------------------------
    """

    retorno_: dict = {}

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    # Tenta 3 vezes a requisição post
    # -------------------------------

    for _ in range(3):

        retorno_ = await retryPOST(url_, data_, headers_)

        if retorno_ != {}:
            break

    return retorno_


async def retryPOST(router_: str, data_: dict, headers_: dict = None) -> dict:
    try:
        async with aiohttp.ClientSession() as session:

            async with session.post(
                    router_,
                    json=data_,
                    headers=headers_
            ) as resp:
                try:
                    return await resp.json()
                except:
                    status = resp.status
                    return {'status': status}

    except Exception as e:
        print("Except with post", e)

    await asyncio.sleep(1)

    return {}

# -----------------------------
# Funções fetchPost + retryPost + PROXY
# -----------------------------


async def fetchPOSTproxy(url_: str, data_: dict, headers_: dict, proxy_: str) -> dict:
    """
    ----------------------------------------------------
    fetch: Requisita assincronamente por método post
    :param headers_: dict
    :param url_: str
    :param data_: dict
    :return: dict
    ----------------------------------------------------
    """

    retorno_: dict = {}

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    # Tenta 3 vezes a requisição post
    # -------------------------------

    for _ in range(3):

        retorno_ = await retryPOSTproxy(url_, data_, headers_, proxy_)

        if retorno_ != {}:
            break

    return retorno_


async def retryPOSTproxy(router_: str, data_: dict, headers_: dict, proxy_: str) -> dict:
    try:

        #proxy = aiohttp.ProxyConnector(proxy=proxy_)

        async with aiohttp.ClientSession() as session:

            async with session.post(
                    router_,
                    json=data_,
                    headers=headers_,
                    proxy=proxy_
            ) as resp:
                try:
                    return await resp.json()
                except:
                    status = resp.status
                    return {'status': status}

    except Exception as e:
        print("Except with post", e)

    await asyncio.sleep(1)

    return {}





# -----------------------------
# Funções fetchPut + retryPut
# -----------------------------


async def fetchPUT(url_: str, data_: dict, headers_: dict = None) -> dict:
    """
    ----------------------------------------------------
    fetch: Requisita assincronamente por método put
    :param headers_: dict
    :param url_: str
    :param data_: dict
    :return: dict
    ----------------------------------------------------
    """

    retorno_: dict = {}

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    # Tenta 3 vezes a requisição put
    # -------------------------------

    for _ in range(3):

        retorno_ = await retryPUT(url_, data_, headers_)

        if retorno_ != {}:
            break

    return retorno_


async def retryPUT(router_: str, data_: dict, headers_: dict = None) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    router_,
                    json=data_,
                    headers=headers_
            ) as resp:
                try:
                    return await resp.json()
                except:
                    msg = await resp.read()
                    return {'message': msg, 'code': 400}

    except Exception as e:
        print("Except with put", e)

    await asyncio.sleep(1)

    return {}


async def retryPUT2(router_: str, data_: dict, headers_: dict = None) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    router_,
                    json=data_,
                    headers=headers_
            ) as resp:
                try:
                    return await resp.json()
                except:
                    return await resp.text()

    except Exception as e:
        print("Except with put", e)

    return {}


#
# Função assincrona para busca do token nos serviços de autorização da Prodesp
# --------------------------------------------------


async def fetchAuthorization(router_: str, data_: dict, headers_: dict = None) -> dict:
    """
    ----------------------------------------------------
    fetchAuthorization: Busca o token nos serviços de autorização do Detran
    :param router_: str
    :param data_: dict
    :param headers_: dict
    :return: json
    ----------------------------------------------------
    """

    form_data_ = aiohttp.FormData()
    form_data_.add_field("client_secret", data_.get("client_secret"))
    form_data_.add_field("client_id", data_.get("client_id"))
    form_data_.add_field("grant_type", data_.get("grant_type"))
    form_data_.add_field("scope", data_.get("scope"))

    if headers_ is None:
        headers_ = {
            'Content-Type': "application/x-www-form-urlencoded",
            "Accept": "*/*",
        }

    return_ = {}

    #
    # Realiza 3 tentativas para obter o retorno do webservice
    # -------------------------------------------------------

    for _ in range(3):

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        router_,
                        data=form_data_,
                        headers=headers_
                ) as resp:
                    result = await resp.json(loads=json.loads)
                    return result

        except Exception as e:
            print("Get api error ", e)
            await asyncio.sleep(0.5)

    return return_


# função genérica assincrôna fetch método post
# --------------------------------

async def fetch(router_: str, data_: dict, headers_: dict = None) -> dict:
    """
    ----------------------------------------------------
    fetch: Requisita assincronamente por método post
    :param headers_: dict
    :param router_: str
    :param data_: dict
    :return: json
    ----------------------------------------------------
    """

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    return_ = {}

    try:
        async with aiohttp.ClientSession() as session:

            async with session.post(
                    router_,
                    json=data_,
                    headers=headers_
            ) as resp:
                return await resp.json()
                # break

    except Exception as e:
        print("Fetch error ", e)
        await asyncio.sleep(0.5)

    return return_


#
# Curadoria
# -----------------


async def fetchVanzolini(router_: str, data_: dict, headers_: dict = None) -> dict:
    """
    ----------------------------------------------------
    fetchVanzolini: Requisita metodo post da webservice da Vanzolini
    :param headers_: dict
    :param router_: str
    :param data_: dict
    :return: json
    ----------------------------------------------------
    """

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    return_ = {}

    try:
        async with aiohttp.ClientSession() as session:

            async with session.post(
                    router_,
                    json=data_,
                    headers=headers_
            ) as resp:
                return await resp.text()
                # break

    except HTTPServerError.HTTPServiceUnavailable:
        await asyncio.sleep(0.5)

    except HTTPServerError.HTTPGatewayTimeout:
        await asyncio.sleep(0.5)

    except HTTPError.HTTPRequestTimeout:
        await asyncio.sleep(0.5)

    return return_


# Formata data atual
# ---------------------------

def getNow():
    """
    getNow: descrição
    :return: data-time
    """
    now_ = datetime.now()
    return now_.today().strftime('%Y-%m-%d')


# -----------------------------
# Remove caracteres indesejados
# -----------------------------

def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string


class TimeoutHTTPAdapter(HTTPAdapter):
    """
            Nome            : TimeoutHTTPAdapter
            Parametro_1     : HTTPAdapter
            Criada          : junho-2021
            Descrição       : faz...
    ____________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self, *args, **kwargs):
        """
        nome: __init__
        :param args: tuple, Any
        :param kwargs: str
        """
        self.timeout = config('DEFAULT_TIMEOUT')
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        """
        nome: send
        :param request: request
        :param kwargs: str
        :return: super().send(request, **kwargs)
        """
        timeout_ = kwargs.get("timeout")
        if timeout_ is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


def splitDict(prekey_: str, context_: dict):
    context_tratado_: dict = {}

    try:

        for context_pai_key_, context_pai_val_ in context_.items():
            if isinstance(context_pai_val_, dict):
                for context_filho_key_, value_filho_val_ in context_[context_pai_key_].items():
                    context_tratado_[prekey_ + context_filho_key_] = value_filho_val_
            elif isinstance(context_pai_val_, list):
                for i in range(len(context_[context_pai_key_])):
                    if isinstance(context_[context_pai_key_][i], dict):
                        for context_filho_key_, value_filho_val_ in context_[context_pai_key_][i].items():
                            context_tratado_[
                                prekey_ + context_pai_key_ + "_" + context_filho_key_ + "_" + str(i)] = value_filho_val_
                    else:
                        context_tratado_[prekey_ + context_pai_key_ + "_" + str(i)] = context_[context_pai_key_][i]
            else:
                context_tratado_[prekey_ + context_pai_key_] = context_pai_val_

    except Exception as e:
        print("Erro na função split dict", e)
        pass

    return context_tratado_


def expiryValidation(expires: str, first: str) -> dict:
    """
    nome: expiryValidation
    :param expires: str
    :param first: str
    :return: dict
    """

    format = "%Y-%m-%d"
    expires = datetime.strptime(expires, format)
    first = datetime.strptime(first, format)
    delta = timedelta(days=395)
    expires_days = expires - first

    return_ = {
        "expired": expires_days < delta,
        "since_expired": expires_days if expires_days > delta else 0
    }

    return return_


async def fetchPOSTBasicAuth(url_: str, data_: dict, headers_: dict = None, UserName_: str = None,
                             password_: str = None) -> dict:
    """
    ----------------------------------------------------
    fetch: Requisita assincronamente por método post
    :param headers_: dict
    :param url_: str
    :param data_: dict
    :return: dict
    ----------------------------------------------------
    """

    retorno_: dict = {}

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    # Tenta 3 vezes a requisição post
    # -------------------------------

    for _ in range(3):

        retorno_ = await retryPOSTBasicAuth(url_, data_, headers_, UserName_, password_)

        if retorno_ != {}:
            break

    return retorno_


async def retryPOSTBasicAuth(router_: str, data_: dict, headers_: dict, UserName_: str, password_: str) -> dict:
    try:
        auth = aiohttp.BasicAuth(UserName_, password_, encoding='utf-8')

        async with aiohttp.ClientSession(auth=auth) as session:

            async with session.post(
                    router_,
                    json=data_,
                    headers=headers_
            ) as resp:
                return await resp.json()

    except Exception as e:
        print("Except witn post", e)

    await asyncio.sleep(1)

    return {}

async def fetchGETBasicAuth(url_: str, data_: dict, headers_: dict, UserName_: str, password_: str) -> dict:
    """
    ----------------------------------------------------
    descrição : Função assincrôna fetchGET método Get
    :param headers_:
    :param url_: str
    :return: json
    ----------------------------------------------------
    """

    retorno_: dict = {}

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    #
    # Tenta 3 vezes a requisição get
    # -------------------------------

    for _ in range(3):

        retorno_ = await retryGETBasicAuth(url_, data_, headers_, UserName_, password_)

        if retorno_ != {}:
            break

    return retorno_


async def retryGETBasicAuth(url_: str, data_: dict, headers_: dict, UserName_: str, password_: str) -> dict:
    try:
        auth = aiohttp.BasicAuth(UserName_, password_, encoding='utf-8')
        async with aiohttp.ClientSession(auth=auth) as session:

            async with session.get(url=url_) as resp:

                try:
                    # Retorno do tipo JSON
                    return await resp.json()

                except:
                    try:
                        # Retorno do tipo binário
                        data_ = await resp.read()
                        dict_str = data_.decode("UTF-8")
                        return ast.literal_eval(dict_str)

                    except:
                        # Retorno do tipo Text
                        return await resp.text()

    except Exception as e:
        print("Except with get ", e)

        return {'code', e}


async def fetchPUTBasicAuth(url_: str, data_: dict, headers_: dict = None, UserName_: str = None,
                            password_: str = None) -> dict:
    """
    ----------------------------------------------------
    fetch: Requisita assincronamente por método post
    :param headers_: dict
    :param url_: str
    :param data_: dict
    :return: dict
    ----------------------------------------------------
    """

    retorno_: dict = {}

    if headers_ is None:
        headers_ = {'Content-Type': 'application/json'}

    # Tenta 3 vezes a requisição post
    # -------------------------------

    for _ in range(3):

        retorno_ = await retryPUTBasicAuth(url_, data_, headers_, UserName_, password_)

        if retorno_ != {}:
            break

    return retorno_


async def retryPUTBasicAuth(router_: str, data_: dict, headers_: dict, UserName_: str, password_: str) -> dict:
    try:
        auth = aiohttp.BasicAuth(UserName_, password_, encoding='utf-8')
        print("passando", router_, data_, headers_)
        async with aiohttp.ClientSession(auth=auth) as session:
            async with session.put(
                    router_,
                    json=data_,
                    headers=headers_
            ) as resp:
                try:
                    return await resp.json()
                except:
                    msg = await resp.read()
                    return {'message': msg, 'code': 400}


    except Exception as e:
        print("Except with put", e)

    await asyncio.sleep(1)

    return {}


# pdf
# ----------------


def createPDF(base64_img, file):
    repository_ = settings.REPOSITORY
    base64_bytes = base64_img.encode('utf-8')
    with open(repository_ + file + ".pdf", 'wb') as file_to_save:
        decoded_image_data = b64decode(base64_bytes)
        file_to_save.write(decoded_image_data)

    return repository_ + file


def removeFile():
    for diretorio, subpastas, arquivos in os.walk('./media'):
        day = str(date.today()-timedelta(1))
        for arquivo in arquivos:
            if day == arquivo.split("#")[0]:
                os.remove(f'./media/{arquivo}')


def generate_numbers() -> str:
    random_value = uuid.uuid4().hex
    nome_file = random_value
    return nome_file.replace(".", "")


def generator() -> str:
    return f'{date.today()}#{uuid.uuid4().hex}'


# from reportlab.pdfgen import canvas

def createPDFPadrao2(texto, file):
    repository_ = settings.REPOSITORY

    with open(repository_ + file + ".txt", 'w') as file_to_save:
        file_to_save.write(texto)
        file_to_save.close()

    return repository_ + file


# from fpdf import FPDF

def createPDFPadrao(texto, file):
    repository_ = settings.REPOSITORY
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font('Arial', 'B', 16)
    #
    # pdf.multi_cell(0, 5, texto)
    #
    # pdf.output(repository_ + 'tuto1.pdf', 'F')

    with open(repository_ + 'tuto1.pdf', 'wb') as f:
        f.write(texto)
    f.close()

    return repository_ + file


def date_parser_formatter(texto: str) -> str:
    res = re.search(r'\b(\d{1,2})[\/\-]*(\d{1,2})[\/\-]*(\d{2}(?:\d{2})?)\b', texto)

    if res:
        dia, mes, ano = res.groups()
        hoje = date.today()
        anoAtual = str(hoje.year)[-2:]
        if len(ano) == 4:
            dataformatada = f'{dia}/{mes}/{ano}'
        else:
            preAno = '19' if ano > anoAtual else '20'
            dataformatada = f'{dia}/{mes}/{preAno}{ano}'
        return re.sub(r'(\b\d{1,2}[\/\-]*\d{1,2}[\/\-]*\d{2}(?:\d{2})?\b)', dataformatada, texto)
    else:
        return texto
