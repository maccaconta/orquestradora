from middle.consumers.serv_agendamento_medico_capital_micro_regiao import ServiceAgendamentoMedicoCapitalMicroRegiao
from middle.consumers.serv_auth import ServiceAuth
from middle.consumers.serv_cadastro_cidadao import ServiceCadastroCidadao
from middle.consumers.serv_confirmacao_agendamento import ServiceConfirmacaoAgendamento
from middle.consumers.serv_consultaExameToxicologico import ServiceConsultaExameToxicologico
from middle.consumers.serv_consulta_rg import ServiceConsultaRG
from middle.consumers.serv_dadosBiograficos import ServiceDadosBiograficos
from middle.consumers.serv_endpoint_vanzolini import ServiceEndpointVanzolini
from middle.consumers.serv_gerar_renach import ServiceGerarRenach
from middle.consumers.serv_gravar_dados_cidadao import ServiceGravarDadosCidadao
from middle.consumers.serv_pagamento_taxa import ServicePagtoTaxa
from middle.consumers.serv_historico_pontos import ServiceHistoricoPontos
from middle.consumers.serv_poupinha_link_certificado_digital import ServicePoupinhaLinkCertificadoDigital
from middle.consumers.serv_precadastro_primeira_habilitacao import ServicePreCadatroPrimeiraHabilitacao
from middle.consumers.serv_realizar_agendamento_medico_psicologico import ServiceRealizarAgendamentoMedicoPsicologico
from middle.consumers.serv_restricoes_debitos import ServiceRestricoesDebitos
from middle.consumers.serv_registro_roubo_furto import ServiceRegistroRouboFurto
from middle.consumers.serv_endereco_para_entrega import ServiceEnderecoParaEntrega
from middle.consumers.serv_exibir_dados_pessoais import ServiceExibirDadosPessoais
from middle.consumers.serv_agendamento_medico_capital import ServiceAgendamentoMedicoCapital
from middle.consumers.serv_buscar_data_agendamento_medico import ServiceBuscarDataAgendamentoMedico
from middle.consumers.serv_agendamento_psicologico_capital import ServiceAgendamentoPsicologicoCapital
from middle.consumers.serv_buscar_data_agendamento_psicologico import ServiceBuscarDataAgendamentoPsicologico
from middle.consumers.serv_busca_cep_cadastro import ServiceBuscaCepCadastro
from middle.consumers.serv_formulario_pendencia import ServiceFormularioPendencia
from middle.consumers.serv_busca_endereco import ServiceBuscaEndereco
from middle.consumers.serv_cadastro_cep_endereco import ServiceCadastroCepEndereco
from middle.consumers.serv_consulta_rebaixamento import ServiceConsultaRebaixamento
from middle.consumers.serv_atualizar_dados_cadastro import ServiceAtualizarDadosCadastro
from middle.consumers.serv_cadastro_endereco_recebimento import ServiceCadastroEnderecoRecebido
from middle.consumers.serv_buscar_horario_agendamento_medico import ServiceBuscarHorarioAgendamentoMedico
from middle.consumers.serv_buscar_horario_agendamento_psicologico import ServiceBuscarHorarioAgendamentoPsicologico
from middle.consumers.serv_retorno_suspensao import ServiceRetornoSuspensao
from middle.consumers.serv_processo_cumprimento_suspensao import ServiceProcessoComprimentoSuspensao
from middle.consumers.serv_realizar_agendamento_medico_renovacao import ServiceRealizarAgendamentoMedicoRenovacao
from middle.consumers.serv_consulta_cadastro import ServiceConsultaCadastro
from middle.consumers.serv_data_agendamento_poupatempo import ServiceDataAgendamentoPoupatempo
from middle.consumers.serv_meus_agendamentos import ServiceMeusAgendamentos
from middle.consumers.serv_horario_agendamento_poupatempo import ServiceHorarioAgendamentoPoupatempo
from middle.consumers.serv_solicitar_segunda_via_cnh import ServiceSolicitarSegundaViaCnh
from middle.consumers.serv_envia_telefone_email import ServiceEnviaTelefoneEmail
from middle.consumers.serv_acompanhamento_emissao_rg import ServiceAcompanhamentoEmissaoRg
from middle.consumers.serv_validade_cnh import ServiceValidadeCnh
from middle.consumers.serv_solicita_cnh_definitiva import ServiceSolicitaCnhDefinitiva
from middle.consumers.serv_enviar_token import ServiceEnviarToken
from middle.consumers.serv_validar_token import ServiceValidarToken
from middle.consumers.serv_inicio_cumprimento_suspensao import ServiceInicioCumprimentoSuspensao
from middle.consumers.serv_encontrar_processos import ServiceEncontrarProcessos
from middle.consumers.serv_consulta_basica_condutor import ServiceConsultaBasicaCondutor
from middle.consumers.serv_consulta_situacao_condutor import ServiceConsultaSituacaoCondutor
from middle.consumers.serv_agendamentos import ServiceAgendamentos
from middle.consumers.serv_postos_poupatempo import ServicePostosPoupatempo
from middle.consumers.serv_certidao_negativa import ServiceCertidaoNegativa
from middle.consumers.serv_enviar_antecedente import ServiceEnviarAntecedente
from middle.consumers.serv_valida_cep import ServiceValidaCep
from middle.consumers.serv_consulta_cep_condutor import ServiceConsultaCepCondutor
from middle.consumers.serv_consulta_base_iirgd import ServiceConsultaBaseIirgd
from middle.consumers.serv_consulta_codigo_cidade_pais import ServiceConsultaCodigoCidadePais
from middle.consumers.serv_postos_id import ServicePostosId
from middle.consumers.serv_rebaixamento_categoria import ServiceRebaixamentoCategoria
from middle.consumers.serv_cep_poupatempo import ServiceCepPoupatempo
from middle.consumers.serv_consultar_segunda_via import ServiceConsultarSegundaVia
from middle.consumers.serv_restricao_aac import ServiceRestricaoAAC
from middle.consumers.serv_antecedentes_criminais import ServiceAntecedentesCriminais
from middle.consumers.serv_consultar_pontos import ServiceConsultarPontos
from middle.consumers.serv_data_feriado import ServiceDataFeriado
from middle.consumers.serv_valida_cpf import ServiceValidaCpf
from middle.consumers.serv_checar_validade_cnh import ServiceChecarValidadeCnh
from middle.consumers.serv_valida_rg import ServiceValidaRg


class Consumers(ServiceCadastroCidadao,
                ServiceDadosBiograficos,
                ServiceAuth,
                ServicePoupinhaLinkCertificadoDigital,
                ServicePagtoTaxa,
                ServiceHistoricoPontos,
                ServiceConsultaExameToxicologico,
                ServicePreCadatroPrimeiraHabilitacao,
                ServiceRestricoesDebitos,
                ServiceRegistroRouboFurto,
                ServiceEnderecoParaEntrega,
                ServiceExibirDadosPessoais,
                ServiceAgendamentoMedicoCapital,
                ServiceBuscarDataAgendamentoMedico,
                ServiceAgendamentoPsicologicoCapital,
                ServiceBuscarDataAgendamentoPsicologico,
                ServiceBuscaCepCadastro,
                ServiceFormularioPendencia,
                ServiceBuscaEndereco,
                ServiceCadastroCepEndereco,
                ServiceConsultaRebaixamento,
                ServiceAtualizarDadosCadastro,
                ServiceCadastroEnderecoRecebido,
                ServiceBuscarHorarioAgendamentoMedico,
                ServiceBuscarHorarioAgendamentoPsicologico,
                ServiceRetornoSuspensao,
                ServiceProcessoComprimentoSuspensao,
                ServiceAgendamentoMedicoCapitalMicroRegiao,
                ServiceRealizarAgendamentoMedicoPsicologico,
                ServiceConfirmacaoAgendamento,
                ServiceConsultaRG,
                ServiceGravarDadosCidadao,
                ServiceGerarRenach,
                ServiceRealizarAgendamentoMedicoRenovacao,
                ServiceConsultaCadastro,
                ServiceDataAgendamentoPoupatempo,
                ServiceMeusAgendamentos,
                ServiceHorarioAgendamentoPoupatempo,
                ServiceSolicitarSegundaViaCnh,
                ServiceEnviaTelefoneEmail,
                ServiceAcompanhamentoEmissaoRg,
                ServiceValidadeCnh,
                ServiceSolicitaCnhDefinitiva,
                ServiceEnviarToken,
                ServiceValidarToken,
                ServiceInicioCumprimentoSuspensao,
                ServiceEncontrarProcessos,
                ServiceConsultaBasicaCondutor,
                ServiceConsultaSituacaoCondutor,
                ServiceEndpointVanzolini,
                ServiceAgendamentos,
                ServicePostosPoupatempo,
                ServiceCertidaoNegativa,
                ServiceEnviarAntecedente,
                ServiceValidaCep,
                ServiceConsultaCepCondutor,
                ServiceConsultaBaseIirgd,
                ServiceConsultaCodigoCidadePais,
                ServicePostosId,
                ServiceRebaixamentoCategoria,
                ServiceCepPoupatempo,
                ServiceConsultarSegundaVia,
                ServiceRestricaoAAC,
                ServiceAntecedentesCriminais,
                ServiceConsultarPontos,
                ServiceDataFeriado,
                ServiceValidaCpf,
                ServiceChecarValidadeCnh,
                ServiceValidaRg):

    def __init__(self):
        super().__init__()

    @property
    def configuration(self, **kwargs):
        """
        name: configuration
        :param kwargs: str
        :return: pass
        """
        pass
