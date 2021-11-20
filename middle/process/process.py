from middle.process.proc9047_inicio_cumprimento_suspensao import Proc9047InicioCumprimentoSuspensao
from middle.process.proc5000_acesso_discovery import Proc5000AcessoDiscovery
from middle.process.proc9020_valida_cep import Proc9020ValidaCep
from middle.process.proc9200_orquest_verifica_servico_habilitacao import Proc9200OrchestVerificaServicoHabilitacao
from middle.process.proc9015_pagamento_taxa import Proc9015TaxaPagtoCNH
from middle.process.proc9021_precadastro_primeira_habilitacao import Proc9021PrecadastroPrimeiraHabilitacao
from middle.process.proc9037_gravar_dados_cidadao import Proc9037GravarDadosCidadao
from middle.process.proc9050_consultar_exame_toxicologico import Proc9050ConsultaExameToxicologico
from middle.process.proc9005_consulta_rg import Proc9005ConsultarRG
from middle.process.proc9012_confirmacao_agendamento import Proc9012ConfirmacaoAgendamento
from middle.process.proc9013_realizar_agendamento_medico_psicologico import Proc9013RealizarAgendamentoMedicoPsicologico
from middle.process.proc9038_gerar_renach import Proc9038GerarRenach
from middle.process.proc999_link_certificado_digital import Proc999LinkCertificadoDigital
from middle.process.proc_consultar_restricoes import ProcConsultarMultasRestricoes
from middle.process.proc_validar_cadastro import ProcValidarCadastro
from middle.process.proc001_historico_pontos import Proc001HistoricoPontos
from middle.process.proc9002_consultar_pontos import Proc9002ConsultarPontos
from middle.process.proc9003_restricoes_debitos import Proc9003RestricoesDebitos
from middle.process.proc004_registro_roubo_furto import Proc004RegistroRouboFurto
from middle.process.proc9006_endereco_para_entrega import Proc9006EnderecoParaEntrega
from middle.process.proc9007_exibir_dados_pessoais import Proc9007ExibirDadosPessoais
from middle.process.proc9008_agendamento_medico_capital import Proc9008AgendamentoMedicoCapitalRegiao
from middle.process.proc9009_buscar_data_agendamento_medico import Proc9009BuscarDataAgendamentoMedico
from middle.process.proc010_agendamento_psicologico_capital import Proc010AgendamentoPsicologicoCapital
from middle.process.proc9011_buscar_data_agendamento_psicologico import Proc9011BuscarDataAgendamentoPsicologico
from middle.process.proc9022_busca_cep_cadastro import Proc9022BuscaCepCadastro
from middle.process.proc9023_formulario_pendencia import Proc9023FormularioPendencia
from middle.process.proc024_busca_endereco import Proc024BuscaEndereco
from middle.process.proc025_cadastro_cep_endereco import Proc025CadastroCepEndereco
from middle.process.proc9026_consulta_rebaixamento import Proc9026ConsultaRebaixamento
from middle.process.proc9027_agendamento_medico_capital_micro_regiao  import Proc9027AgendamentoMedicoCapitalMicroRegiao
from middle.process.proc9028_atualizar_dados_cadastro import Proc9028AtualizarDadosCadastro
from middle.process.proc9030_cadastro_endereco_recebimento import Proc9030CadastroEnderecoRecebimento
from middle.process.proc9031_buscar_horario_agendamento_medico import Proc9031BuscarHorarioAgendamentoMedico
from middle.process.proc9032_buscar_horario_agendamento_psicologico import Proc9032BuscarHorarioAgendamentoPsicologico
from middle.process.proc033_retorno_suspensao import Proc033RetornoSuspensao
from middle.process.proc034_processo_cumprimento_suspensao import Proc034ProcessoCumprimentoSuspensao
from middle.process.proc9010_realizar_agendamento_medico_renovacao import Proc9010RealizarAgendamentoMedicoRenovacao
from middle.process.proc9040_solicitar_segunda_via_cnh import Proc9040SolicitarSegundaViaCnh
from middle.process.proc0002_consulta_cadastro import Proc0002ConsultaCadastro
from middle.process.proc0004_data_agendamento_poupatempo import Proc0004DataAgendamentoPoupatempo
from middle.process.proc0001_meus_agendamentos import Proc0001MeusAgendamentos
from middle.process.proc0005_horario_agendamento_poupatempo import Proc0005HorarioAgendamentoPoupatempo
from middle.process.proc9016_endpoint_vanzolini import proc9016_endpoint_vanzolini
from middle.process.proc9014_envia_telefone_email import Proc9014EnviaTelefoneEmail
from middle.process.proc0007_acompanhamento_emissao_rg import Proc0007AcompanhamentoEmissaoRg
from middle.process.proc9042_validade_cnh import Proc9042ValidadeCnh
from middle.process.proc9039_solicita_cnh_definitiva import Proc9039SolicitaCnhDefinitiva
from middle.process.proc9035_enviar_token import Proc9035EnviarToken
from middle.process.proc9036_validar_token import proc9036ValidarToken
from middle.process.proc9047_inicio_cumprimento_suspensao import Proc9047InicioCumprimentoSuspensao
from middle.process.proc9043_encontrar_processos import Proc9043EncontrarProcessos
from middle.process.proc9044_consulta_basica_condutor import Proc9044ConsultaBasicaCondutor
from middle.process.proc9045_consulta_situacao_condutor import Proc9045ConsultaSituacaoCondutor
from middle.process.proc0008_agendamento import Proc0008Agendamentos
from middle.process.proc0009_postos_poupatempo import Proc0009PostosPoupatempo
from middle.process.proc0010_certidao_negativo import Proc0010CertidaoNegativa
from middle.process.proc0011_enviar_antecedente import Proc0011EnviarAntecedente
from middle.process.proc9048_consulta_cep_condutor import Proc9048ConsultaCepCondutor
from middle.process.proc9046_consulta_base_iirgd import Proc9046ConsultaBaseIirgd
from middle.process.proc0012_postos_id import Proc0012PostosId
from middle.process.proc_clean_proc import ProcCleanProc
from middle.process.proc9051_consulta_municipio_pais import Proc9051ConsultaMunicipioPais
from middle.process.proc9049_rebaixamento_categoria import Proc9049RebaixamentoCategoria
from middle.process.proc0006_cep_poupatempo import Proc0006CepPoupatempo
from middle.process.proc9052_consultar_segunda_via import Proc9052ConsultarSegundaVia
from middle.process.proc0013_restricao_aac import Proc0013RestricaoAAC
from middle.process.proc0003_antecedentes_criminais import Proc0003AntecedentesCriminais
from middle.process.proc0014_data_feriado import Proc0014DataFeriado
from middle.process.proc0015_valida_cpf import Proc0015ValidaCpf
from middle.process.proc0016_checar_validade_cnh import Proc0016ChecarValidadeCnh
from middle.process.proc0017_valida_rg import Proc0017ValidaRg


class Process(ProcValidarCadastro,
              ProcConsultarMultasRestricoes,
              Proc999LinkCertificadoDigital,
              Proc9015TaxaPagtoCNH,
              Proc001HistoricoPontos,
              Proc9050ConsultaExameToxicologico,
              Proc9021PrecadastroPrimeiraHabilitacao,
              Proc9002ConsultarPontos,
              Proc9003RestricoesDebitos,
              Proc004RegistroRouboFurto,
              Proc9006EnderecoParaEntrega,
              Proc9007ExibirDadosPessoais,
              Proc9008AgendamentoMedicoCapitalRegiao,
              Proc9009BuscarDataAgendamentoMedico,
              Proc010AgendamentoPsicologicoCapital,
              Proc9011BuscarDataAgendamentoPsicologico,
              Proc9012ConfirmacaoAgendamento,
              Proc9013RealizarAgendamentoMedicoPsicologico,
              Proc9022BuscaCepCadastro,
              Proc9023FormularioPendencia,
              Proc024BuscaEndereco,
              Proc025CadastroCepEndereco,
              Proc9026ConsultaRebaixamento,
              Proc9027AgendamentoMedicoCapitalMicroRegiao,
              Proc9028AtualizarDadosCadastro,
              Proc9030CadastroEnderecoRecebimento,
              Proc9031BuscarHorarioAgendamentoMedico,
              Proc9032BuscarHorarioAgendamentoPsicologico,
              Proc9200OrchestVerificaServicoHabilitacao,
              Proc033RetornoSuspensao,
              Proc034ProcessoCumprimentoSuspensao,
              Proc9005ConsultarRG,
              Proc9037GravarDadosCidadao,
              Proc9038GerarRenach,
              Proc9010RealizarAgendamentoMedicoRenovacao,
              Proc9040SolicitarSegundaViaCnh,
              Proc0002ConsultaCadastro,
              Proc0004DataAgendamentoPoupatempo,
              Proc0001MeusAgendamentos,
              Proc0005HorarioAgendamentoPoupatempo,
              Proc9014EnviaTelefoneEmail,
              Proc0007AcompanhamentoEmissaoRg,
              Proc9042ValidadeCnh,
              Proc9039SolicitaCnhDefinitiva,
              Proc9035EnviarToken,
              proc9036ValidarToken,
              Proc9047InicioCumprimentoSuspensao,
              Proc9043EncontrarProcessos,
              Proc9044ConsultaBasicaCondutor,
              Proc9045ConsultaSituacaoCondutor,
              proc9016_endpoint_vanzolini,
              Proc0008Agendamentos,
              Proc0009PostosPoupatempo,
              Proc0010CertidaoNegativa,
              Proc0011EnviarAntecedente,
              Proc5000AcessoDiscovery,
              Proc9020ValidaCep,
              Proc9048ConsultaCepCondutor,
              Proc9046ConsultaBaseIirgd,
              Proc0012PostosId,
              ProcCleanProc,
              Proc9051ConsultaMunicipioPais,
              Proc9049RebaixamentoCategoria,
              Proc0006CepPoupatempo,
              Proc9052ConsultarSegundaVia,
              Proc0013RestricaoAAC,
              Proc0003AntecedentesCriminais,
              Proc0014DataFeriado,
              Proc0015ValidaCpf,
              Proc0016ChecarValidadeCnh,
              Proc0017ValidaRg):

    def __init__(self):
        super().__init__()
