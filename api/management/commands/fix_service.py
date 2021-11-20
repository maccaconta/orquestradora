from django.core.management.base import BaseCommand
from api.models import Service


class Command(BaseCommand):
    """
             Name            : Cr
            :param           : BaseCommand
            :create          : junho-2021
            description      : faz...
    ____________________________________________________________________________________________________
    """
    help = 'Valor default da configuração das chamadas dos serviços de API Detran'

    def handle(self, **options):
        """
         name: handle
        :param options:
        :return: ...
        """
        self.stdout.write('Deletando dados de Service')
        Service.objects.all().delete()

        self.stdout.write('Criando dados Default dos Serviços CNH')
        Service.objects.create(service="cnh",
                               url_serv_prod="https://www.poupatempo4g.sp.gov.br/ppt4g-rest-detran-cnh/api/v1",
                               url_serv_homo="http://homologa.poupatempo4g.sp.gov.br/ppt4g-rest-detran-cnh/api/v1",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Poupatempo.Acesso")

        self.stdout.write('Criando dados Default dos Serviços CRV')
        Service.objects.create(service="crv",
                               url_serv_prod="https://www.poupatempo4g.sp.gov.br/ppt4g-rest-detran-crv/api/v1",
                               url_serv_homo="http://homologa.poupatempo4g.sp.gov.br/ppt4g-rest-detran-crv/api/v1",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Poupatempo.Acesso")

        self.stdout.write('Criando dados Default dos Serviços CAR')
        Service.objects.create(service="car",
                               url_serv_prod="https://www.car.api.sp.gov.br/api/car/",
                               url_serv_homo="http://homolog.car.api.sp.gov.br/api/car/",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Car.Search Car.AgendaSP.Upsert AgendaSP.Search AgendaSP.Upsert Evento.Enviar")
        self.stdout.write('Criando dados Default dos Serviços eagenda')
        Service.objects.create(service="eagenda",
                               url_serv_prod="https://www.agendasp.sp.gov.br/eagenda.api",
                               url_serv_homo="http://eagendamento.homologacao.sp.gov.br/eagenda.api",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Car.Search Car.AgendaSP.Upsert AgendaSP.Search AgendaSP.Upsert Evento.Enviar")

        self.stdout.write('Criando dados Default dos Serviços eagenda')
        Service.objects.create(service="eagenda2",
                               url_serv_prod="https://www.agendasp.sp.gov.br/eagenda.api/v1",
                               url_serv_homo="http://eagendamento.homologacao.sp.gov.br/eagenda.api/v1",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="0e5f0b27-d9e6-44c3-b551-0128870afffb",
                               client_id="agendasp",
                               grant_type="client_credentials",
                               scope="Car.Search Car.AgendaSP.Upsert AgendaSP.Search AgendaSP.Upsert Evento.Enviar")

        self.stdout.write('Criando dados Default dos Serviços antecedentes')
        Service.objects.create(service="antecedentes",
                               url_serv_prod="http://novo.desenvolvimentoportal.poupatempo.sp.gov.br/wps/PA_cidadao.web.servic",
                               url_serv_homo="https://homologa.poupatempo.sp.gov.br/wps/PA_cidadao.web.servic",
                               url_auth_prod="",
                               url_auth_homo="",
                               client_secret="atestAntecedentes@123",
                               client_id="atestAntecedentes",
                               grant_type="",
                               scope="")

        self.stdout.write('Criando dados Default dos Serviços pge')
        Service.objects.create(service="pge",
                               url_serv_prod="https://www.poupatempo4g.sp.gov.br/ppt4g-rest-pge/api/v1/",
                               url_serv_homo="http://homologa.poupatempo4g.sp.gov.br/ppt4g-rest-pge/api/v1/",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Prefeitura.Consultar")

        self.stdout.write('Criando dados Default dos Serviços iirgd')
        Service.objects.create(service="iirgd",
                               url_serv_prod="https://www.poupatempo4g.sp.gov.br/ppt4g-rest-iirgd/api/v1",
                               url_serv_homo="http://homologa.poupatempo4g.sp.gov.br/ppt4g-rest-iirgd/api/v1",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Poupatempo.Acesso")

        Service.objects.create(service="sms",
                               url_serv_prod="https://www.poupatempo4g.sp.gov.br/ppt4g-rest-utils/api/v1",
                               url_serv_homo="http://homologa.poupatempo4g.sp.gov.br/ppt4g-rest-utils/api/v1",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Poupatempo.Acesso")

        Service.objects.create(service="discovery",
                               url_serv_prod="",
                               url_serv_homo="",
                               url_auth_prod="",
                               url_auth_homo="",
                               client_secret="",
                               client_id="",
                               grant_type="",
                               scope="")

        self.stdout.write('Criando dados Default dos Serviços de CEP')
        Service.objects.create(service="cep",
                               url_serv_prod="http://10.200.117.42:8080/prodesp-cep.api/api/cep/",
                               url_serv_homo="http://10.200.45.234/prodesp-cep.api/api/cep",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token",
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Poupatempo.Acesso")

        self.stdout.write('Criando dados Default dos Serviços de base do IIRGD')
        Service.objects.create(service="base_iirgd",
                               url_serv_prod="http://www.hnprd.dipol.prodesp.sp.gov.br/IIRGD_Detran/ep/Home",
                               url_serv_homo="http://10.200.44.2/IIRGD_Detran/ep/Home",
                               url_auth_prod="https://www.autenticador.sp.gov.br/connect/token",
                               url_auth_homo="http://homolog.autenticador.sp.gov.br/connect/token", 
                               client_secret="135e63a4-6102-4d89-93fd-ce4e3c22708f",
                               client_id="OrquestradorPoupinha",
                               grant_type="client_credentials",
                               scope="Poupatempo.Acesso")

        self.stdout.write('Criando dados Default dos Serviços feriados')
        Service.objects.create(service="feriados",
                               url_serv_prod="https://intranet.poupatempo.sp.gov.br",
                               url_serv_homo="http://intranet.poupatempo.sp.gov.br",
                               url_auth_prod="",
                               url_auth_homo="",
                               client_secret="N@d3J5pRd",
                               client_id="fullcalendar",
                               grant_type="",
                               scope="")