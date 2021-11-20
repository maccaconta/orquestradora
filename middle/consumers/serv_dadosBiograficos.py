import requests
import json
from requests.packages.urllib3.util.retry import Retry
from api.utilities import TimeoutHTTPAdapter


class ServiceDadosBiograficos:

    @staticmethod
    def serv_dados_biograficos():
        """
        nome: serv_dados_biograficos
        :return: ...
        """
        json_: dict
        url_: str
        headers_: dict
        retries_: object

        json_ = {"cpf": "13692400829",
                 "renach": "SP500230234",
                 "reuso": "S"}

        url_ = 'http:10.2.24.70//homologacao.e-cnhsp.sp.gov.br/eaigefor/DadosBiograficosService/DadosBiograficosService.wsdl'
        headers_ = {"Accept": "application/json", "Content-Type": "application/xml"}

        retries_ = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])

        adapter_ = TimeoutHTTPAdapter(max_retries=retries_)

        session_ = requests.Session()
        session_.mount('http://homologacao.e-cnhsp.sp.gov.br', adapter_)
        session_.mount('htts://homologacao.e-cnhsp.sp.gov.br', adapter_)

        try:
            request_ = session_.get(url_, headers=headers_, json=json_, auth=("13692400829", "123456"))
            request_.raise_for_status()

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
