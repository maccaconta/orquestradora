from django.core.management.base import BaseCommand
from api.models import Routers


class Command(BaseCommand):
    """
             Name            : Command
            :param           : BaseCommand
            :create          : junho-2021
            description      : faz...
    ____________________________________________________________________________________________________
    """
    help = 'Valor default da configuração do Routers'

    def handle(self, **options):
        """
         name: handle
        :param options:
        :return: ...
        """

        # # TODO: armazenar URL
        self.stdout.write('Deletando dados de Routers')
        Routers.objects.all().delete()
        
        self.stdout.write('Criando dados Default do Routers')
        Routers.objects.create(process="PROC999",
                               url="/orchest/v1/middle/proc999/",
                               service="cnh")
        
        self.stdout.write('Criando dados de Taxas')
        Routers.objects.create(process="PROC9015_PAGAMENTO_TAXA",
                               url="/orchest/v1/middle/proc9015/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta de Pontos')
        Routers.objects.create(process="PROC001_HISTORICO_PONTOS",
                               url="/orchest/v1/middle/proc001/")
        
        self.stdout.write('Criando dados para Consulta RG')
        Routers.objects.create(process="PROC9002_CONSULTAR_PONTOS",
                               url="/orchest/v1/middle/proc9002/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta RG')
        Routers.objects.create(process="PROC9003_RESTRICOES_DEBITOS",
                               url="/orchest/v1/middle/proc9003/",
                               service="crv")
        
        self.stdout.write('Criando dados para Consulta de registro de roubo e furto')
        Routers.objects.create(process="PROC004_REGISTRO_ROUBO_FURTO",
                               url="/orchest/v1/middle/proc004/")
        
        self.stdout.write('Criando dados para Consulta RG')
        Routers.objects.create(process="PROC9005_CONSULTA_RG",
                               url="/orchest/v1/middle/proc9005/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta de registro de endereço de entrega')
        Routers.objects.create(process="PROC9006_ENDERECO_PARA_ENTREGA",
                               url="/orchest/v1/middle/proc9006/",
                               service="cnh"
                               )
        
        self.stdout.write('Criando dados para Consulta exibir dados pessoais')
        Routers.objects.create(process="PROC9007_EXIBIR_DADOS_PESSOAIS",
                               url="/orchest/v1/middle/proc9007/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta de agendamento medico capital')
        Routers.objects.create(process="PROC9008_AGENDAMENTO_MEDICO_CAPITAL_REGIAO",
                               service="cnh",
                               url="/orchest/v1/middle/proc9008/")
        
        self.stdout.write('Criando dados para Consulta de busca de data do agendamento medico')
        Routers.objects.create(process="PROC9009_BUSCAR_DATA_AGENDAMENTO_MEDICO",
                               service="cnh",
                               url="/orchest/v1/middle/proc9009/")
        
        self.stdout.write('Criando dados para Consulta do agendamento psicologico capital')
        Routers.objects.create(process="PROC010_AGENDAMENTO_PSICOLOGICO_CAPITAL",
                               url="/orchest/v1/middle/proc010/")
        
        self.stdout.write('Criando dados para Consulta de busca de data do agendamento psicologico')
        Routers.objects.create(process="PROC9011_BUSCAR_DATA_AGENDAMENTO_PSICOLOGICO",
                               service="cnh",
                               url="/orchest/v1/middle/proc9011/")
        
        Routers.objects.create(process="PROC9012_CONFIRMACAO_AGENDAMENTO",
                               service="cnh",
                               url="/orchest/v1/middle/proc9012/")
        
        self.stdout.write('Criando dados para Consulta de busca de cep cadastrado')
        Routers.objects.create(process="PROC022_BUSCA_CEP_CADASTRO",
                               url="/orchest/v1/middle/proc022/")
        
        self.stdout.write('Criando dados para Consulta do formulario pendencia')
        Routers.objects.create(process="PROC9023_FORMULARIO_PENDENCIA",
                               url="/orchest/v1/middle/proc9023/",
                               service="crv")
        
        self.stdout.write('Criando dados para Consulta de busca de endereco')
        Routers.objects.create(process="PROC024_BUSCA_ENDERECO",
                               url="/orchest/v1/middle/proc024/")
        
        self.stdout.write('Criando dados para Consulta de cadastro de cep endereco')
        Routers.objects.create(process="PROC025_CADASTRO_CEP_ENDERECO",
                               url="/orchest/v1/middle/proc025/")
        
        self.stdout.write('Criando dados para Consulta de rebaixamento')
        Routers.objects.create(process="PROC9026_CONSULTA_REBAIXAMENTO",
                               url="/orchest/v1/middle/proc9026/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta agendamento medico capital micro regiao')
        Routers.objects.create(process="PROC9027_AGENDAMENTO_MEDICO_CAPITAL_MICRO_REGIAO",
                               url="/orchest/v1/middle/proc9027/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta de atualizar dados de cadastro')
        Routers.objects.create(process="PROC9028_ATUALIZAR_DADOS_CADASTRO",
                               url="/orchest/v1/middle/proc9028/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta de cadastro de endereco de recebimento')
        Routers.objects.create(process="PROC9030_CADASTRO_ENDERECO_RECEBIMENTO",
                               service="cnh",
                               url="/orchest/v1/middle/proc9030/")
        
        self.stdout.write('Criando dados para Consulta de busca de horario para agendamento medico')
        Routers.objects.create(process="PROC9031_BUSCAR_HORARIO_AGENDAMENTO_MEDICO",
                               service="cnh",
                               url="/orchest/v1/middle/proc9031/")
        
        self.stdout.write('Criando dados para Consulta de busca de horario para agendamento psicologico')
        Routers.objects.create(process="PROC9032_BUSCAR_HORARIO_AGENDAMENTO_PSICOLOGICO",
                               service="cnh",
                               url="/orchest/v1/middle/proc90032/")
        
        self.stdout.write('Criando dados para Gravar Dados cidadão')
        Routers.objects.create(process="PROC9037_GRAVAR_DADOS_CIDADAO",
                               service="cnh",
                               url="/orchest/v1/middle/proc9037/")
        
        self.stdout.write('Criando dados para Geração Renach')
        Routers.objects.create(process="PROC9038_GERAR_RENACH",
                               service="cnh",
                               url="/orchest/v1/middle/proc9038/")
        
        self.stdout.write('Criando dados para Consulta de Exame Toxicológico')
        Routers.objects.create(process="PROC9050_CONSULTA_EXAME_TOXICOLOGICO",
                               url="/orchest/v1/middle/proc9050/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Pré Cadastro Primeira Habilitação')
        Routers.objects.create(process="PROC9021_PRE_CADASTRO_PRIMEIRA_HABILITACAO",
                               url="/orchest/v1/middle/proc9021/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Pré Cadastro Primeira Habilitação')
        Routers.objects.create(process="PROC9200_ORCHEST_VERIFICA_SERVICO_HABILITACAO",
                               url="/orchest/v1/middle/proc9200/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta retorno de suspensao')
        Routers.objects.create(process="PROC033_RETORNO_SUSPENSAO",
                               url="/orchest/v1/middle/proc033/")
        
        self.stdout.write('Criando dados para Consulta processo do cumprimento de suspensao')
        Routers.objects.create(process="PROC034_PROCESSO_CUMPRIMENTO_SUSPENSAO",
                               url="/orchest/v1/middle/proc034/")
        
        self.stdout.write('Criando dados para agendamento de exame medico e psicologico')
        Routers.objects.create(process="PROC9013_REALIZAR_AGENDAMENTO_MEDICO_PSICOLOGICO",
                               url="/orchest/v1/middle/proc9013/",
                               service="cnh")
        
        self.stdout.write('Criando dados para Consulta do cadastro')
        Routers.objects.create(process="PROC0002_CONSULTA_CADASTRO",
                               url="/orchest/v1/middle/proc0002/",
                               service="car")
        
        self.stdout.write('Criando dados para Consulta da para agendamento no poupatempo')
        Routers.objects.create(process="PROC0004_DATA_AGENDAMENTO_POUPATEMPO",
                               url="/orchest/v1/middle/proc0004/",
                               service="eagenda")

        self.stdout.write('Criando dados para Consulta dos meus agendamentos')
        Routers.objects.create(process="PROC0001_MEUS_AGENDAMENTOS",
                               url="/orchest/v1/middle/proc0001/",
                               service="eagenda")
        
        self.stdout.write('Criando dados para Consulta dos meus agendamentos')
        Routers.objects.create(process="PROC0005_HORARIO_AGENDAMENTO_POUPATEMPO",
                               url="/orchest/v1/middle/proc0005/",
                               service="eagenda")
        
        self.stdout.write('Criando dados para agendamento de exame medico para renovação')
        Routers.objects.create(process="PROC9010_REALIZAR_AGENDAMENTO_MEDICO_RENOVACAO",
                               url="/orchest/v1/middle/proc9010/",
                               service="cnh")
        self.stdout.write('Criando dados para Consulta de busca de cep cadastrado')
        Routers.objects.create(process="PROC9022_BUSCA_CEP_CADASTRO",
                               url="/orchest/v1/middle/proc9022/",
                               service= "crv")
        
        self.stdout.write('Criando dados para solicitação de segunda via de CNH')
        Routers.objects.create(process="PROC9040_SOLICITAR_SEGUNDA_VIA_CNH",
                               url="/orchest/v1/middle/proc9040/",
                               service="cnh")
        
        self.stdout.write('Criando dados para registro de contato do cidadão')
        Routers.objects.create(process="PROC9014_ENVIA_TELEFONE_EMAIL",
                               url="/orchest/v1/middle/proc9014/",
                               service="cnh")
        
        self.stdout.write('Criando dados para acompanhamento de emissão de RG')
        Routers.objects.create(process="PROC0007_ACOMPANHAMENTO_EMISSAO_RG",
                               url="/orchest/v1/middle/proc0007/",
                               service="iirgd")
        
        self.stdout.write('Criando dados para consulta das datas da primeira CNH')
        Routers.objects.create(process="PROC9042_VALIDADE_CNH",
                               url="/orchest/v1/middle/proc9042/",
                               service="cnh")
        
        self.stdout.write('Criando dados para solicitação de CNH definitiva')
        Routers.objects.create(process="PROC9039_SOLICITA_CNH_DEFINITIVA",
                               url="/orchest/v1/middle/proc9039/",
                               service="cnh")

        self.stdout.write('Criando dados de envio de token')
        Routers.objects.create(process="PROC9035_ENVIAR_TOKEN",
                               url="/orchest/v1/middle/proc9035/",
                               service="sms")

        self.stdout.write('Criando dados para validação de token')
        Routers.objects.create(process="PROC9036_VALIDAR_TOKEN",
                               url="/orchest/v1/middle/proc9036/",
                               service="sms")

        self.stdout.write('Criando dados para inicio de cunprimento de suspensão')
        Routers.objects.create(process="PROC9047_INICIO_CUMPRIMENTO_SUSPENSAO",
                               url="/orchest/v1/middle/proc9047/",
                               service="cnh")

        self.stdout.write('Criando dados para encontro de processos')
        Routers.objects.create(process="PROC9043_ENCONTRAR_PROCESSOS",
                               url="/orchest/v1/middle/proc9043/",
                               service="cnh")
   
        self.stdout.write('Criando dados para consulta básica de informações sobre o condutor')
        Routers.objects.create(process="PROC9044_CONSULTA_BASICA_CONDUTOR",
                               url="/orchest/v1/middle/proc9044/",
                               service="cnh")

        self.stdout.write('Criando dados para consulta da situação do condutor')
        Routers.objects.create(process="PROC9045_CONSULTA_SITUACAO_CONDUTOR",
                               url="/orchest/v1/middle/proc9045/",
                               service="cnh")

        self.stdout.write('Criando dados para Curadoria Vanzolini')
        Routers.objects.create(process="PROC9016_ENDPOINT_VANZOLINI",
                               url="/orchest/v1/middle/proc9016/",
                               service="discovery")

        self.stdout.write('Criando dados para Criar agendamentos')
        Routers.objects.create(process="PROC0008_AGENDAMENTO",
                               url="/orchest/v1/middle/proc0008/",
                               service="eagenda2")

        self.stdout.write('Criando dados para Consulta os postos de atendimento')
        Routers.objects.create(process="PROC0009_POSTOS_POUPATEMPO",
                               url="/orchest/v1/middle/proc0009/",
                               service="eagenda")

        self.stdout.write('Criando dados para Consulta certidao negativo')
        Routers.objects.create(process="PROC0010_CERTIDAO_NEGATIVA",
                               url="/orchest/v1/middle/proc0010/",
                               service="pge")

        self.stdout.write('Criando dados para o envio por email')
        Routers.objects.create(process="PROC0011_ENVIAR_ANTECEDENTE",
                               url="/orchest/v1/middle/proc0011/",
                               service="antecedentes")

        self.stdout.write('Criando dados para Consulta do Discovery')
        Routers.objects.create(process="PROC5000_ACESSO_DISCOVERY",
                               url="/orchest/v1/middle/proc5000/",
                               service="discovery")
        
        self.stdout.write('Criando dados para consulta da situação do condutor')
        Routers.objects.create(process="PROC9020_VALIDA_CEP",
                               url="/orchest/v1/middle/proc9020/",
                               service="cnh")
        
        self.stdout.write('Criando dados para consulta de CEP do condutor')
        Routers.objects.create(process="PROC9046_CONSULTA_BASE_IIRGD",
                               url="/orchest/v1/middle/proc9046/",
                               service="base_iirgd")
        
        self.stdout.write('Criando dados para consulta postos poupatempo')
        Routers.objects.create(process="PROC0012_POSTOS_ID",
                               url="/orchest/v1/middle/proc0012/",
                               service="eagenda")
        
        self.stdout.write('Criando dados para consulta de CEP do condutor')
        Routers.objects.create(process="PROC9048_CONSULTA_CEP_CONDUTOR",
                               url="/orchest/v1/middle/proc9048/",
                               service="cep")

        self.stdout.write('Criando dados para limpar procs')
        Routers.objects.create(process="PROC_CLEAN",
                               url="/orchest/v1/middle/proc_clean/",
                               service="cnh")

        self.stdout.write('Criando dados para Consulta de rebaixamento')
        Routers.objects.create(process="PROC9049_REBAIXAMENTO_CATEGORIA",
                               url="/orchest/v1/middle/proc9049/",
                               service="cnh")

        self.stdout.write('Criando dados para consulta de endereço pelo CEP')
        Routers.objects.create(process="PROC0006_CEP_POUPATEMPO",
                               url="/orchest/v1/middle/proc0006/",
                               service="cep")

        self.stdout.write('Criando dados para consulta restriçao em antecedentes criminais')
        Routers.objects.create(process="PROC0013_RESTRICAO_AAC",
                               url="/orchest/v1/middle/proc0013/",
                               service="antecedentes")

        self.stdout.write('Criando dados para consulta  atentado de antecedentes criminais')
        Routers.objects.create(process="PROC0003_ANTECEDENTES_CRIMINAIS",
                               url="/orchest/v1/middle/proc0003/",
                               service="antecedentes")

        self.stdout.write('Consultar validade da CNH')
        Routers.objects.create(process="PROC9052_CONSULTAR_SEGUNDA_VIA",
                               url="/orchest/v1/middle/proc9052/",
                               service="cnh")

        self.stdout.write('Consultar data de feriado')
        Routers.objects.create(process="PROC0014_DATA_FERIADO",
                               url="/orchest/v1/middle/proc0014/",
                               service="feriados")

        self.stdout.write('Consultar validade da cpf')
        Routers.objects.create(process="PROC0015_VALIDA_CPF",
                               url="/orchest/v1/middle/proc0015/",
                               service="cnh")

        self.stdout.write('Consultar validade da documentos')
        Routers.objects.create(process="PROC0016_CHECAR_VALIDADE_CNH",
                               url="/orchest/v1/middle/proc0016/",
                               service="cnh")

        self.stdout.write('Consultar validade da rg')
        Routers.objects.create(process="PROC0017_VALIDA_RG",
                               url="/orchest/v1/middle/proc0017/",
                               service="cnh")

        self.stdout.write('Consultar o municipio do pais')
        Routers.objects.create(process="PROC9051_CONSULTA_MUNICIPIO_PAIS",
                               url="/orchest/v1/middle/proc9050/",
                               service="cnh")
