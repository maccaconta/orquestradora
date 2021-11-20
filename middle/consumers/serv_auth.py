import certifi
import requests
import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from urllib3 import ProxyManager, make_headers
import urllib3
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from requests.auth import HTTPProxyAuth, HTTPBasicAuth


class ServiceAuth:
    @staticmethod
    def func_auth():
        """
        name: func_auth
        :return: HttpResponse
        """
        url_: str
        params_: dict
        proxies_: dict

        s = requests.Session()

        url_ = 'http://10.200.240.83/onda-1/v1/auth'

        params_ = {
            "password": "totem",
            "scope": "CONSULTA_CONDUTOR_RECICLAGEM",
            "username": "totem"
        }

        proxies_ = {
            "http": "http://200.144.4.103:443",
            "https": "https://200.144.4.103:443"
        }

        header_ = 'Content-Type: application/json'

        # s.auth = ("13692400829", "123456")
        # s.proxies = _proxies

        r = s.post(url_, json=params_)  # <------------------ 1 consulta do token

        print(r.text)

        token_ = json.loads(r.text)

        # ----------------------

        s2 = requests.Session()

        url_ = 'http://10.200.240.83/onda-1/rest/condutor/consulta/reciclagem/cpf/13692400829'

        headers_ = {'Authorization': token_['access_token']}

        r2_ = s2.get(url_, headers=headers_,
                     auth=HTTPBasicAuth('13692400829', '123456'))  # <------------consulta do servico

        print(r2_)

        return HttpResponse(token_['access_token'])

    # permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated
    #
    # url = 'homologacao.e-cnhsp.sp.gov.br/eaigefor/DadosBiograficosService/DadosBiograficosService.wsdl'
    #
    # par = '?cpf=13692400829&renavh=SP500230234&reuso=N'
    #
    # default_headers = make_headers(proxy_basic_auth='14200629801:Prodesp@2021')
    #
    # http = urllib3.ProxyManager('http://200.144.4.103:443', headers=default_headers)
    #
    # r = http.request('GET', url)
    #
    # print(r.headers)
    # print(r)
    #
    # return HttpResponse(r, content_type='text/xml')

    # s = requests.Session()
    #
    # proxies = {
    #     "http": "http://200.144.4.103:443",
    #     "https": "http://200.144.4.103:443"
    # }
    #
    # auth = HTTPProxyAuth("14200629801", "Prodesp@2021")
    #
    # s.proxies = proxies
    # s.auth = auth
    #
    # r = s.get('http://homologacao.e-cnhsp.sp.gov.br/eaigefor/DadosBiograficosService/DadosBiograficosService.wsdl')
    #
    # return HttpResponse(r.text, content_type='text/xml')
