from api.utilities import run_async, splitDict
from middle.consumers.consumers import Consumers


class Proc9021PrecadastroPrimeiraHabilitacao(Consumers):

    async def setPrecadastroPrimeiraHabilitacao(request) -> dict:
        """
         name: setPrecadastroPrimeiraHabilitacao
        :param request: dict
        :return: dict
        """
        params_: dict = {}
        dtstring_: str = ""
        nacionalidade_: str = ""
        codigo_entidade_: str = ""
        context_: dict = {}
        retorno_: dict = {}

        try:

            #
            # Tratamento da Chamada
            #

            # Todo:
            # Separar apenas as variáveis de contexto necessárias para o serviço
            # Tratar parâmetros conforme o swegger do serviço
            celular = str(request["parameters"].get("numero_celular"))
            dddcel = celular[:2]
            numcel = celular[2:]
            telefone = str(request["parameters"].get("numero_telefone"))
            dddtel = telefone[:2]
            numtel = telefone[2:]
            params_["cpf"] = str(request["parameters"].get("cpf", ""))
            params_["bairro"] = str(request["parameters"].get("bairro", ""))
            params_["categoria_pretendida"] = str(request["parameters"].get("categoria_pretendida", ""))
            params_["celular"] = numcel
            params_["cep"] = str(request["parameters"].get("cep", ""))
            params_["complemento"] = str(request["parameters"].get("complemento", ""))
            params_["ddd_celular"] = dddcel
            params_["ddd_telefone"] = dddtel
            params_["email"] = str(request["parameters"].get("email", ""))
            params_["logradouro"] = str(request["parameters"].get("logradouro", ""))
            params_["naturalidade"] = str(request["parameters"].get("naturalidade", ""))  # 3550308
            params_["nome"] = str(request["parameters"].get("nome", ""))
            params_["nome_mae"] = str(request["parameters"].get("nome_mae", ""))
            params_["nome_pai"] = str(request["parameters"].get("nome_pai", ""))
            params_["numero_carteira_militar"] = str(request["parameters"].get("numero_carteira_militar", ""))
            params_["numero_documento"] = str(request["parameters"].get("numero_documento", ""))
            params_["orgao_documento"] = str(request["parameters"].get("orgao_documento", ""))
            params_["numero"] = str(request["parameters"].get("numero", ""))
            params_["telefone"] = numtel
            params_["tipo_documento"] = str(request["parameters"].get("tipo_documento", ""))
            params_["num_RNE"] = str(request["parameters"].get("num_RNE", ""))
            params_["orgao_RNE"] = str(request["parameters"].get("orgao_RNE", ""))

            #
            # Tratamento Uppercase
            # ---------------------------

            params_["sexo"] = str(request["parameters"].get("sexo", "")).upper()
            params_["uf_documento"] = str(request["parameters"].get("uf_documento", "SP")).upper()
            params_["uf_RNE"] = str(request["parameters"].get("uf_RNE", "")).upper()

            # Tratamento Sim ou Nao
            # ---------------------------

            params_["autoriza_email"] = "S" \
                if str(request["parameters"].get("autoriza_email", "SIM")).upper() == "SIM" else "N"

            params_["autoriza_sms"] = "S" \
                if str(request["parameters"].get("autoriza_sms", "SIM")) == "SIM" else "N"

            params_["pretende_atividade_remunerada"] = "S" \
                if str(request["parameters"].get("pretende_atividade_remunerada", "SIM")).upper() == "SIM" \
                else "N"

            params_["necessidade_veiculo_adaptado"] = "S" \
                if str(request["parameters"].get("necessidade_veiculo_adaptado", "SIM")) == "SIM" else "N"

            # -----------------------------
            # Tratamento data de nascimento para aaaa-mm-dd
            # ------------------------------

            dtstring_ = str(request["parameters"].get("data_nascimento", ""))

            if len(dtstring_) == 10:
                params_["data_nascimento"] = dtstring_[6:10] + "-" + dtstring_[3:5] + "-" + dtstring_[0:2]
            else:
                params_["data_nascimento"] = ""

            # -----------------------------
            # Tratamento diversos nacionalidade
            # -----------------------------

            nacionalidade_ = str(request["parameters"].get("nacionalidade", "brasileiro")).lower()

            if nacionalidade_ == 'brasileiro':
                params_["nacionalidade"] = "BRASILEIRA"

            elif nacionalidade_ == 'brasileiro naturalizado':
                params_["nacionalidade"] = "NATURALIZADO"

            elif nacionalidade_ == 'estrangeiro':
                params_["nacionalidade"] = "ESTRANGEIRO"

            elif nacionalidade_ == 'brasileiro nascido no exterior':
                params_["nacionalidade"] = "BRASILEIRO_NASCIDO_EXTERIOR"

            # Tratamento codigo_entidade
            # --------------------------------

            codigo_entidade_ = str(request["parameters"].get("codigo_entidade", ""))

            if codigo_entidade_ == 'Exército':
                params_["codigo_entidade"] = "EXERCITO"

            elif codigo_entidade_ == 'Marinha':
                params_["codigo_entidade"] = "MARINHA"

            elif codigo_entidade_ == 'Aeronáutica':
                params_["codigo_entidade"] = "AERONAUTICA"

            elif codigo_entidade_ == 'Polícia militar':
                params_["codigo_entidade"] = "POLICIA_MILITAR"

            elif codigo_entidade_ == 'Polícia civil':
                params_["codigo_entidade"] = "POLICIA_CIVIL"

            else:
                params_["codigo_entidade"] = "NENHUM"

            #
            # Chamada do serviço Prodesp
            # ------------------

            context_ = await Consumers.servSetPreCadatroPrimeiraHabilitacao(params_, request["service"])

        except:
            print("Erro na criação dos parâmetros na PROC")

        #
        # Tratamento do Retorno
        #

        if context_ == {}:
            retorno_ = {
                'text': 'api_nok',
                'context': {}
            }

        else:

            try:

                try:
                    context_['mensagem'] = context_['mensagem'].lower()
                except:
                    pass

                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9021_", context_)

                cod_ = int(context_tratado_['proc9021_codigo'])

                if cod_ == 0:

                    retorno_ = {
                        'text': 'api_ok',
                        'context': context_tratado_
                    }

                else:

                    # Cep
                    # ---------------

                    if cod_ == 2:

                        retorno_ = {
                            'text': 'api_erro',
                            'context': context_tratado_
                        }

                        retorno_["context"]["cep"] = ""

                    # Data Nascimento
                    # ---------------

                    elif cod_ == 21:

                        retorno_ = {
                            'text': 'api_erro',
                            'context': context_tratado_
                        }

                        retorno_["context"]["data_nascimento"] = ""

                    # Condutor não pode exercer atividade remunerada
                    # ----------------------------------------------

                    elif cod_ == 374:

                        retorno_ = {
                            'text': 'api_nok',
                            'context': context_tratado_
                        }

                    # email ou UF errados
                    # --------------------

                    elif cod_ == 1101:

                        retorno_ = {
                            'text': 'api_erro',
                            'context': context_tratado_
                        }

                        #  email informado(a) é inválido(a).
                        # ----------------------------------

                        if "email" in context_['mensagem']:
                            retorno_["context"]["email"] = ""

                        # logradouro informado(a) é inválido(a)"
                        # ----------------------------------

                        elif "logradouro" in context_['mensagem']:

                            retorno_["context"]["logradouro"] = ""
                            retorno_["context"]["cep"] = ""
                            retorno_["context"]["bairro"] = ""

                        else:
                            retorno_["context"]["uf_documento"] = ""

                    # erros não previstos
                    # --------------------

                    else:

                        retorno_ = {
                            'text': 'api_nok',
                            'context': context_tratado_
                        }
            except:

                retorno_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }

        retorno_["context"]["process"] = ""
        
        return retorno_
