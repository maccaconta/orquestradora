from middle.models import CityCode, CountryCode


class ServiceConsultaCodigoCidadePais:

    @staticmethod
    def serv_consulta_codigo_cidade_pais(param) -> dict:
        retorno_: dict = {}

        try:
            print("Parâmetros da requisição:", param)
        except Exception as e:
            print("Dados da requisição não foram enviados para consulta do serviço", e)
            return {}

        try:
            if param['type'] == 'cidade':
                aux = CityCode.objects.get(city_name=param['name'])
                retorno_ = aux.city_code
            elif param['type'] == 'pais':
                aux = CountryCode.objects.get(country_name=param['name'].upper())
                retorno_ = aux.country_code
            else:
                retorno_ = {}

            print("Retorno da API:", retorno_)

        except Exception as e:
            print(f'Error:{e}')
            retorno_ = {}

        return retorno_
