from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response

from api.utilities import run_async
from middle.process.process import Process
import json
import urllib3

from django.http import HttpResponse
import os
from pathlib import Path

urllib3.disable_warnings()


class ApiValidarCadastro(APIView, Process):
    """
                 Name            : ApiValidarCadastro
                :class           : Classe ApiValidarCadastro
                 create          : junho-2021
                :param           : APIView
                :param           : Process
                description      : This API aims to validate the Registration in the conversation flow
                                   on Citizen's Day
        ___________________________________________________________________________________________________
        Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
        """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
        name: post
        description: metodo post da API
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = Process.proc_validar_cadastro(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiMultasRestricoes(APIView, Process):
    """
             Name            : ApiMultasRestricoes
            :class           : Classe ApiMultasRestricoes
             create          : junho-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to validate the Registration in the conversation flow
                               on Citizen's Day
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = json.loads(request.data)
        return_ = Process.proc_multas_restricoes(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiLinkCertificado(APIView, Process):
    """
             Name            : ApiMultasRestricoes
            :class           : Classe ApiMultasRestricoes
            :create          : junho-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to validate the Registration in the conversation flow
                               on Citizen's Day
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = Process.get_certificado_digitial(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiPagamentoTaxa(APIView, Process):
    """
             Name            : ApiPagamentoTaxa
            :class           : Classe ApiPagamentoTaxa
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the values of a generation of any generated tax
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = run_async(Process.get_valores_taxa, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiHistoricoPontos(APIView, Process):
    """
             Name            : ApiHistoricoPontos
            :class           : Classe ApiHistoricoPontos
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to retrieve the points of a Citzen license
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = run_async(Process.get_consultar_pontos, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultarPontos(APIView, Process):
    """
             Name            : ApiExibirDadosPessoais
            :class           : Classe ApiExibirDadosPessoais
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the personal data of a Citizen
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consultar_pontos, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)
        


class ApiRestricoesDebitos(APIView, Process):
    """
            Name            : ApiRestricoesDebitos
            :class           : Classe ApiRestricoesDebitos
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the restrictions and/or debit registered on a vehicle
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_restricoes_debitos, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiRegistroRouboFurto(APIView, Process):
    """
             Name            : ApiRegistroRouboFurto
            :class           : Classe ApiRegistroRouboFurto
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to register the robbery or theft of a vehicle
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = Process.get_registro_roubo_furto(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiEnderecoParaEntrega(APIView, Process):
    """
             Name            : ApiEnderecoParaEntrega
            :class           : Classe ApiEnderecoParaEntrega
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to retrieve the delivery address for documents
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_endereco_para_entrega, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiExibirDadosPessoais(APIView, Process):
    """
             Name            : ApiExibirDadosPessoais
            :class           : Classe ApiExibirDadosPessoais
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the personal data of a Citizen
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    
    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_exibir_dados_pessoais, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiAgendamentoMedicoCapitalRegiao(APIView, Process):
    """
             Name            : ApiAgendamentoMedicoCapital
            :class           : Classe ApiAgendamentoMedicoCapital
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to register a doctor appointment in the capital
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request_, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_: dict
        return_: dict
        request_ = request_.data
        return_ = run_async(Process.get_agendamento_medico_capital, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiAgendamentoPsicologicoCapital(APIView, Process):
    """
             Name            : ApiAgendamentoPsicologicoCapital
            :class           : Classe ApiAgendamentoPsicologicoCapital
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to register a psychologist appointment in the capital
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = Process.get_agendamento_psicologico_capital(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiBuscarDataAgendamentoPsicologico(APIView, Process):
    """
             Name            : ApiBuscarDataAgendamentoPsicologico
            :class           : Classe ApiBuscarDataAgendamentoPsicologico
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available dates for a psychologist appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):

        """
        name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_buscar_data_agendamento_psicologico, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiBuscaCepCadastro(APIView, Process):
    """
             Name            : ApiBuscaCepCadastro
            :class           : Classe ApiBuscaCepCadastro
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to retrieve the postal code registered for the Citizen
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = run_async(Process.get_busca_cep_cadastro, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiFormularioPendencia(APIView, Process):
    """
             Name            : ApiFormularioPendencia
            :class           : Classe ApiFormularioPendencia
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to register the answers to the pendencies form
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """


    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = run_async(Process.get_formulario_pendencia, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiBuscaEndereco(APIView, Process):
    """
             Name            : ApiBuscaEndereco
            :class           : Classe ApiBuscaEndereco
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to retrieve the address in the citizen's register
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = Process.get_busca_endereco(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiCadastroCepEndereco(APIView, Process):
    """
             Name            : ApiCadastroCepEndereco
            :class           : Classe ApiCadastroCepEndereco
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to register the citizen's address
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = Process.get_cadastro_cep_endereco(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaRebaixamento(APIView, Process):
    """
             Name            : ApiConsultaRebaixamento
            :class           : Classe ApiConsultaRebaixamento
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to retrieve the information about the driver's license downgrade
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated
    @staticmethod
    def post(request, *args, **kwargs):
        """
        name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consulta_rebaixamento, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiAtualizarDadosCadastro(APIView, Process):
    """
             Name            : ApiAtualizarDadosCadastro
            :class           : Classe ApiAtualizarDadosCadastro
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to update the citizen's registration data
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """


    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = run_async(Process.get_atualizar_dados_cadastro,request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiCadastroEnderecoRecebimento(APIView, Process):
    """
             Name            : ApiCadastroEnderecoRecebimento
            :class           : Classe ApiCadastroEnderecoRecebimento
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to register the delivery address
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_cadastro_endereco_recebimento, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiBuscarHorarioAgendamentoMedico(APIView, Process):
    """
             Name            : ApiBuscarHorarioAgendamentoMedico
            :class           : Classe ApiBuscarHorarioAgendamentoMedico
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available schedules for a doctor appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_buscar_horario_agendamento_medico, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiBuscarHorarioAgendamentoPsicologico(APIView, Process):
    """
             Name            : ApiBuscarHorarioAgendamentoPsicologico
            :class           : Classe ApiBuscarHorarioAgendamentoPsicologico
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available schedules for a psychologist appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_buscar_horario_agendamento_psicologico, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaExameToxicologico(APIView, Process):
    """
     Name            : ApiConsultaExameToxicologico
    :class           : Classe ApiConsultaExameToxicologico
    :create          : Agosto-2021
    :param           : APIView
    :param           : Process
    description      : This API aims to list the toxicology testing schedule
    ___________________________________________________________________________________________________
    """
    permission_classes = [AllowAny]
    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.getConsultaExameToxicologico, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiPreCadastroPrimeiraHabilitacao(APIView, Process):
    """
     Name            : ApiPreCadastroPrimeiraHabilitacao
    :class           : Classe ApiPreCadastroPrimeiraHabilitacao
    :create          : Agosto-2021
    :param           : APIView
    :param           : Process
    description      : This API aims to register a pre registration for a citizen's first driver's license
    ___________________________________________________________________________________________________
    """
    permission_classes = [AllowAny]
    @staticmethod
    def post(request_, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request_.data
        return_ = run_async(Process.setPrecadastroPrimeiraHabilitacao, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiOrquestVerificaServicoHabilitacao(APIView, Process):
    """
     Name            : ApiPreCadastroPrimeiraHabilitacao
    :class           : Classe ApiPreCadastroPrimeiraHabilitacao
     create          : Agosto-2021
    :param           : APIView
    :param           : Process
    description      : Está processo consume a API de pré cadastro primeira habilitação
    ___________________________________________________________________________________________________
    """
    permission_classes = [AllowAny]
    @staticmethod
    def post(request_, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request_.data
        return_ = run_async(Process.getServicoHabilitacao, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiRetornoSuspensao(APIView, Process):
    """
             Name            : ApiRetornoSuspensao
            :class           : Classe ApiRetornoSuspensao
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to return driver suspensions
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = Process.get_retorno_suspensao(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiProcessoCumprimentoSuspensao(APIView, Process):
    """
             Name            : ApiProcessoCumprimentoSuspensao
            :class           : Classe ApiProcessoCumprimentoSuspensao
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to record a penalty compliance and start date
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """
        request_: dict
        return_: dict

        request_ = request.data
        return_ = Process.get_processo_cumprimento_suspensao(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiOrquestAgendamentoMedicoCapitalMicroRegiao(APIView, Process):
    """
     Name            : ApiPreCadastroPrimeiraHabilitacao
    :class           : Classe ApiPreCadastroPrimeiraHabilitacao
     create          : Agosto-2021
    :param           : APIView
    :param           : Process
    description      : Está processo consume a API de pré cadastro primeira habilitação
    ___________________________________________________________________________________________________
    """
    permission_classes = [AllowAny]
    @staticmethod
    def post(request_, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request_.data
        return_ = run_async(Process.get_agendamento_medico_capital_micro_regiao, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiBuscarDataAgendamentoMedico(APIView, Process):
    """
             Name            : ApiBuscarDataAgendamentoMedico
            :class           : Classe ApiBuscarDataAgendamentoMedico
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available dates for a doctor appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_buscar_data_agendamento_medico, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiRealizarAgendamentoMedicoPsicologico(APIView, Process):
    """
            :class           : ApiRealizarAgendamentoMedicoPsicologico
            :create          : setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available dates for a doctor appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.setRealizarAgendamentoMedicoPsicologico, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConfirmacaoAgendamento(APIView, Process):
    """
            :class           : ApiConfirmacaoAgendamento
            :create          : setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available dates for a doctor appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data

        return_["id_attendance"] = request_["id_attendance"]

        return_ = run_async(Process.getApiConfirmacaoAgendamento, request_)

        return Response(return_)


class ApiConsultaRG(APIView, Process):
    """
            :class           : ApiConsultaRG
            :create          : setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available dates for a doctor appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data

        return_["id_attendance"] = request_["id_attendance"]

        return_ = run_async(Process.getConsultarRG, request_)

        return Response(return_)


class ApiGravarDadosCidadao(APIView, Process):
    """
            :class           : ApiConsultaRG
            :create          : setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available dates for a doctor appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.setGravarDadosCidadao, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiGerarRenach(APIView, Process):
    """
            :class           : ApiGerarRenach
            :create          : Agosto-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the available dates for a doctor appointment
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.getGerarRenach, request_)
        
        
        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaCadastro(APIView, Process):
    """
            :class           : ApiConsultaCadastro
            :create          : Agosto-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list registration
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consulta_cadastro, request_)

        return_["id_attendance"] = request_["id_attendance"]

     
        return Response(return_)


class ApiDataAgendamentoPoupatempo(APIView, Process):
    """
            :class           : ApiConsultaCadastro
            :create          : Agosto-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the dates available for scheduling
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_data_agendamento_poupatempo, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiMeusAgendamentos(APIView, Process):
    """
            :class           : ApiConsultaCadastro
            :create          : Agosto-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the scheduling
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_meus_agendamentos, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiHorariosAgendamentoPoupatempo(APIView, Process):
    """
            :class           : ApiConsultaCadastro
            :create          : Agosto-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the times available for scheduling
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_horario_agendamento_poupatempo, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiRealizaAgendamentoMedicoRenovacao(APIView, Process):
    """
            :class           : ApiConsultaCadastro
            :create          : Agosto-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the times available for scheduling
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_realizar_agendamento_medico_renovacao, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)
        

class ApiSolicitarSegundaViaCnh(APIView, Process):
    """
            :class           : ApiSolicitarSegundaViaCnh
            :create          : Sep-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to create a request for re-issuing the driver's license
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_solicitar_segunda_via_cnh, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)
        

class ApiEnviaTelefoneEmail(APIView, Process):
    """
            :class           : ApiEnviaTelefoneEmail
            :create          : Sep-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to register the citizen's contact information
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_envia_telefone_email, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiAcompanhamentoEmissaoRg(APIView, Process):
    """
            :class           : ApiAcompanhamentoEmissaoRg
            :create          : Agosto-2021
            :param           : APIView
            :param           : Process
            description:     : This API is intended for accompaniment the issuance of RG
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data

        return_ = run_async(Process.get_acompanhamento_emissao_rg, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiIniciarCumprimentoSuspensao(APIView, Process):
    """
            :class           : ApiIniciarCumprimentoSuspensao
            :create          : Agosto-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to request the definitive driver's license
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        
        return_ = run_async(Process.get_inicio_cumprimento_suspensao, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiValidadeCnh(APIView, Process):
    """
            :class           : ApiValidadeCnh
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list information concerning the citizen's first driver's license
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_validade_cnh, request_)

        # return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiSolicitaCnhDefinitiva(APIView, Process):
    """
            :class           : ApiSolicitaCnhDefinitiva
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to request the definitive driver's license
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_solicita_cnh_definitiva, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaBasicaCondutor(APIView, Process):
    """
            :class           : ApiConsultaBasicaCondutor
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the registered information about the driver
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consulta_basica_condutor, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiCuradoriaVanzolini(APIView, Process):
    """
            :class           : ApiCuradoriaVanzolini        
            :create          : Setembro-2021
            :param           : request
            description:     :Enviar serviços não encontrados para curadoria da Vanzolini
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas 
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.proc_endpoint_vanzolini, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaSituacaoCondutor(APIView, Process):
    """
            :class           : ApiConsultaSituacaoCondutor
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the registered information about the driver's situation
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas 
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consulta_situacao_condutor, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaCepCondutor(APIView, Process):
    """
            :class           : ApiConsultaCepCondutor
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the complete address through the postal code
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consulta_cep_condutor, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiAgendamento(APIView, Process):
    """
            :class           : ApiAgendamento
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list schedule
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas 
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_agendamentos, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiPostosPoupatempo(APIView, Process):
    """
            :class           : ApiPostosPoupatempo
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the service stations
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):

        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_postos_poupatempo, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiCertidaoNegativa(APIView, Process):
    """
            :class           : ApiCertidaoNegativa
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API is intended for negative certificate query
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_certidao_negativa, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiEnviarAntecedente(APIView, Process):
    """
            :class           : ApiEnviarAntecedente
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API is intended for sending the criminal record by email
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_enviar_antecedente, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiAcessoDiscovery(APIView, Process):
    """
            :class           : ApiAcessoDiscovery
            Acessa o IBM Discovery
            :create          : Setembro-2021
            :param           : request
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = Process.getDocumentDiscovery (request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaBaseIirgd(APIView, Process):
    """
            :class           : ApiConsultaBaseIirgd
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the driver's information from IIRGD's basis
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consulta_base_iirgd, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiValidaCep(APIView, Process):
    """
             Name            : ApiValidaCep
            :class           : Classe ApiValidaCep
            :create          : setember-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to valited the driver's zip code
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated
    @staticmethod
    def post(request, *args, **kwargs):

        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_valida_cep, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)
        

class ApiConsultaCepCondutor(APIView, Process):
    """
            :class           : ApiConsultaCepCondutor
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the complete address through the postal code
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated
    @staticmethod
    def post(request, *args, **kwargs):

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consulta_cep_condutor, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiPostosID(APIView, Process):
    """
            :class           : ApiPostosID
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list ranks by description
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated
    @staticmethod
    def post(request, *args, **kwargs):

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_postos_id, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiCleanProc(APIView, Process):
    """
            :class           : ApiConsultaCepCondutor
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the complete address through the postal code
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated
    @staticmethod
    def post(request, *args, **kwargs):

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_clean_proc, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiRebaixamentoCategoria(APIView, Process):
    """
            :class           : ApiRebaixamentoCategoria
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the complete address through the postal code
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated
    @staticmethod
    def post(request, *args, **kwargs):

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_rebaixamento_categoria, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiEncontrarProcessos(APIView, Process):
    """
            :class           : ApiEncontrarProcessos
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to request the definitive driver's license
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data

        return_ = run_async(Process.get_encontrar_processos, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaCidadePais(APIView, Process):
    """
            :class           : ApiConsultaCidadePais
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the complete address through the postal code
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated
    @staticmethod
    def post(request, *args, **kwargs):

        request_: dict
        return_: dict
        request_ = request.data
        return_ = Process.get_codigo_municio_pais(request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)

class ApiValidarToken(APIView, Process):
    """
            :class           : ApiValidarToken
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to request the definitive driver's license
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data

        return_ = run_async(Process.get_validar_token, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiEnviarToken(APIView, Process):
    """
            :class           : ApiApiEnviarToken
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to request the definitive driver's license
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_enviar_token, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class UpdateDatabase(APIView):
    
    def __init__(self):
        super().__init__()

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def get(request, *args, **kwargs):
        print(Path(__file__).resolve().parent.parent)
        os.system('fab dev')

        return HttpResponse('')


class ApiCepPoupatempo(APIView, Process):
    """
            :class           : ApiConsultaCepCondutor
            :create          : Setembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to list the complete address through the postal code
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_cep_poupatempo, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)

class ApiConsultarSegundaVia(APIView, Process):
    """
             Name            : ApiConsutarSegundaVia
            :class           : Classe ApiConsutarSegundaVia
            :create          : jul-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to get Cnh's expiration date.
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    
    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_consultar_segunda_via, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)

class ApiRestricaoAAC(APIView, Process):
    """
            :class           : ApiRestricaoAAC
            :create          : Outubro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to verify the restriction of criminal background attestation
     ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas
    """
    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_restricao_aac, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiAntecedentesCriminais(APIView, Process):
    """
            :class           : ApiAntecedentesCriminais
            :create          : Outubro-2021
            :param           : APIView
            :param           : Process
            description:     : This API is intended to query background criminal
  ___________________________________________________________________________________________________

    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_antecedentes_criminais, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiDataFeriado(APIView, Process):
    """
            :class           : ApiDataFeriado
            :create          : Outubro-2021
            :param           : APIView
            :param           : Process
            description:     : This API is intended to query holiday dates
  ___________________________________________________________________________________________________

    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_data_feriado, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiValidaCpf(APIView, Process):
    """
            :class           : ApiValidaCpf
            :create          : Outubro-2021
            :param           : APIView
            :param           : Process
            description:     : This API is intended to validate cpf
  ___________________________________________________________________________________________________

    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_valida_cpf, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiChecarValidadeCnh(APIView, Process):
    """
            :class           : ApiChecarValidadeCnh
            :create          : Novembro-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims to validate CNH expiration dates
  ___________________________________________________________________________________________________

    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_checar_validade_cnh, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)



class ApiValidaRg(APIView, Process):
    """
            :class           : ApiValidaRg
            :create          : Outubro-2021
            :param           : APIView
            :param           : Process
            description:     : This API is intended to validate rg
  ___________________________________________________________________________________________________

    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_valida_rg, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)


class ApiConsultaMunicipioPais(APIView, Process):
    """
             Name            : ApiConsultaMunicipioPais
            :class           : Classe ApiConsultaMunicipioPais
            :create          : nov-2021
            :param           : APIView
            :param           : Process
            description:     : This API aims find the city
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    permission_classes = [AllowAny]  # todo: em produção alterar para IsAuthenticated

    @staticmethod
    def post(request, *args, **kwargs):
        """
         name: post
        :param request: request
        :param args: args
        :param kwargs: str
        :return: dict
        """

        request_: dict
        return_: dict
        request_ = request.data
        return_ = run_async(Process.get_codigo_municio_pais, request_)

        return_["id_attendance"] = request_["id_attendance"]

        return Response(return_)