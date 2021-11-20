from middle.views import ApiMultasRestricoes, ApiRealizaAgendamentoMedicoRenovacao,  ApiValidarCadastro, ApiLinkCertificado, ApiPagamentoTaxa, ApiHistoricoPontos, \
    ApiConsultaExameToxicologico, ApiPreCadastroPrimeiraHabilitacao, \
    ApiConsultarPontos, ApiRestricoesDebitos, ApiRegistroRouboFurto, ApiEnderecoParaEntrega, ApiExibirDadosPessoais, \
    ApiAgendamentoMedicoCapitalRegiao, ApiBuscarDataAgendamentoMedico, ApiAgendamentoPsicologicoCapital, \
    ApiBuscarDataAgendamentoPsicologico, ApiBuscaCepCadastro, ApiFormularioPendencia, ApiBuscaEndereco, \
    ApiCadastroCepEndereco, ApiConsultaRebaixamento, ApiAtualizarDadosCadastro, ApiCadastroEnderecoRecebimento, \
    ApiBuscarHorarioAgendamentoMedico, ApiBuscarHorarioAgendamentoPsicologico, ApiOrquestVerificaServicoHabilitacao, \
    ApiRetornoSuspensao, ApiProcessoCumprimentoSuspensao, ApiOrquestAgendamentoMedicoCapitalMicroRegiao, \
    ApiRealizarAgendamentoMedicoPsicologico, ApiConfirmacaoAgendamento, ApiConsultaRG, ApiGravarDadosCidadao, \
    ApiGerarRenach, ApiConsultaCadastro, ApiDataAgendamentoPoupatempo, ApiMeusAgendamentos, ApiEncontrarProcessos, \
    ApiAcompanhamentoEmissaoRg, ApiValidadeCnh, ApiEnviarToken, ApiValidarToken, \
    ApiIniciarCumprimentoSuspensao, ApiCuradoriaVanzolini, ApiRebaixamentoCategoria, ApiPostosID, \
    ApiHorariosAgendamentoPoupatempo, ApiSolicitarSegundaViaCnh, ApiEnviaTelefoneEmail, \
    ApiSolicitaCnhDefinitiva, ApiConsultaBasicaCondutor, \
    ApiHorariosAgendamentoPoupatempo, ApiSolicitarSegundaViaCnh, ApiEnviaTelefoneEmail, \
    ApiAcompanhamentoEmissaoRg, ApiValidadeCnh, ApiSolicitaCnhDefinitiva, ApiConsultaBasicaCondutor, \
    ApiConsultaSituacaoCondutor, ApiConsultaCepCondutor, ApiConsultaCidadePais, ApiConsultaBaseIirgd, ApiAgendamento, \
    ApiPostosPoupatempo, ApiCertidaoNegativa, ApiEnviarAntecedente, ApiAcessoDiscovery, ApiValidaCep, ApiCleanProc, \
    UpdateDatabase, ApiCepPoupatempo, ApiRestricaoAAC, ApiAntecedentesCriminais, ApiDataFeriado, \
    ApiValidaCpf, ApiChecarValidadeCnh, ApiConsultarSegundaVia, ApiValidaRg , ApiConsultaMunicipioPais

from django.urls import path

urlpatterns = [
    path('proc01/', ApiValidarCadastro.as_view()),
    path('proc999/', ApiLinkCertificado.as_view()),
    path('proc9015/', ApiPagamentoTaxa.as_view()),
    path('proc001/', ApiHistoricoPontos.as_view()),
    path('proc021/', ApiPreCadastroPrimeiraHabilitacao.as_view()),
    path('proc9050/', ApiConsultaExameToxicologico.as_view()),
    path('proc9002/', ApiConsultarPontos.as_view()),
    path('proc9003/', ApiRestricoesDebitos.as_view()),
    path('proc004/', ApiRegistroRouboFurto.as_view()),
    path('proc005/', ApiConsultaRG.as_view()),
    path('proc9006/', ApiEnderecoParaEntrega.as_view()),
    path('proc9007/', ApiExibirDadosPessoais.as_view()),
    path('proc9008/', ApiAgendamentoMedicoCapitalRegiao.as_view()),
    path('proc9009/', ApiBuscarDataAgendamentoMedico.as_view()),
    path('proc010/', ApiAgendamentoPsicologicoCapital.as_view()),
    path('proc9011/', ApiBuscarDataAgendamentoPsicologico.as_view()),
    path('proc9012/', ApiConfirmacaoAgendamento.as_view()),
    path('proc9013/', ApiRealizarAgendamentoMedicoPsicologico.as_view()),
    path('proc9016/', ApiCuradoriaVanzolini.as_view()),
    path('proc9037/', ApiGravarDadosCidadao.as_view()),
    path('proc9038/', ApiGerarRenach.as_view()),
    path('proc9022/', ApiBuscaCepCadastro.as_view()),
    path('proc9023/', ApiFormularioPendencia.as_view()),
    path('proc024/', ApiBuscaEndereco.as_view()),
    path('proc025/', ApiCadastroCepEndereco.as_view()),
    path('proc9026/', ApiConsultaRebaixamento.as_view()),
    path('proc9027/', ApiOrquestAgendamentoMedicoCapitalMicroRegiao.as_view()),
    path('proc9028/', ApiAtualizarDadosCadastro.as_view()),
    path('proc9030/', ApiCadastroEnderecoRecebimento.as_view()),
    path('proc9031/', ApiBuscarHorarioAgendamentoMedico.as_view()),
    path('proc9032/', ApiBuscarHorarioAgendamentoPsicologico.as_view()),
    path('proc200/', ApiOrquestVerificaServicoHabilitacao.as_view()),
    path('proc033/', ApiRetornoSuspensao.as_view()),
    path('proc034/', ApiProcessoCumprimentoSuspensao.as_view()),
    path('proc9010/', ApiRealizaAgendamentoMedicoRenovacao.as_view()),
    path('proc0002/', ApiConsultaCadastro.as_view()),
    path('proc0004/', ApiDataAgendamentoPoupatempo.as_view()),
    path('proc0001/', ApiMeusAgendamentos.as_view()),
    path('proc0005/', ApiHorariosAgendamentoPoupatempo.as_view()),
    path('proc9040/', ApiSolicitarSegundaViaCnh.as_view()),
    path('proc9014/', ApiEnviaTelefoneEmail.as_view()),
    path('proc0007/', ApiAcompanhamentoEmissaoRg.as_view()),
    path('proc9042/', ApiValidadeCnh.as_view()),
    path('proc9042/', ApiSolicitaCnhDefinitiva.as_view()),
    path('proc9035/', ApiEnviarToken.as_view()),
    path('proc9036/', ApiValidarToken.as_view()),
    path('proc9047/', ApiIniciarCumprimentoSuspensao.as_view()),
    path('proc9043/', ApiEncontrarProcessos.as_view()),
    path('proc9044/', ApiConsultaBasicaCondutor.as_view()),
    path('proc9045/', ApiConsultaSituacaoCondutor.as_view()),
    path('proc0008/', ApiAgendamento.as_view()),
    path('proc0009/', ApiPostosPoupatempo.as_view()),
    path('proc0010/', ApiCertidaoNegativa.as_view()),
    path('proc0011/', ApiEnviarAntecedente.as_view()),
    path('proc5000/', ApiAcessoDiscovery.as_view()),
    path('proc9020/', ApiValidaCep.as_view()),
    path('proc9048/', ApiConsultaCepCondutor.as_view()),
    path('proc9046/', ApiConsultaBaseIirgd.as_view()),
    path('proc0012/', ApiPostosID.as_view()),
    path('proc_clean/', ApiCleanProc.as_view()),
    path('proc9051/', ApiConsultaCidadePais.as_view()),
    path('proc9049/', ApiRebaixamentoCategoria.as_view()),
    path('fab/database/', UpdateDatabase.as_view()),
    path('proc0006/', ApiCepPoupatempo.as_view()),
    path('proc9052/', ApiConsultarSegundaVia.as_view()),
    path('proc0013/', ApiRestricaoAAC.as_view()),
    path('proc0003/', ApiAntecedentesCriminais.as_view()),
    path('proc0014/', ApiDataFeriado.as_view()),
    path('proc0015/', ApiValidaCpf.as_view()),
    path('proc0016/', ApiChecarValidadeCnh.as_view()),
    path('proc0017/', ApiValidaRg.as_view()),
    path('proc9051/', ApiConsultaMunicipioPais.as_view()),

    

]
