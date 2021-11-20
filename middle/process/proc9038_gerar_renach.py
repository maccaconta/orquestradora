from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9038GerarRenach(Consumers):

    async def getGerarRenach(request_) -> dict:
        """
        name: setGravarDadosCidadao
        :param request_: request
        :return: dict
        """

        # Todo : não conseguimos ainda testar

        retorno_: dict = {}
        context_: dict = {}
        data_: dict = {}
        params_: dict = {}

        try:

            params_['apresenta_documentos'] = "S"
            params_["autoriza_email"] = "S" \
                if str(request_["parameters"].get("autoriza_email", "SIM")).upper() == "SIM" else "N"

            params_["autoriza_sms"] = "S" \
                if str(request_["parameters"].get("autoriza_sms", "SIM")) == "SIM" else "N"

            params_['bairro'] = str(request_["parameters"].get("bairro"))
            params_['categoria_pretendida'] = str(request_["parameters"].get("categoria_pretendida"))

            params_['cep'] = str(request_["parameters"].get("cep"))
            params_['codigo_entidade'] = "NENHUM"
            params_['coleta_biometrica'] = str(request_["parameters"].get("coleta_obrigatoria", "N"))
            params_['complemento'] = str(request_["parameters"].get("complemento",""))
            params_['cpf'] = str(request_["parameters"].get("cpf"))

            dtstring_ = str(request_["parameters"].get("data_nascimento", ""))

            if len(dtstring_) == 10:
                params_["data_nascimento"] = dtstring_[6:10] + "-" + dtstring_[3:5] + "-" + dtstring_[0:2]
            else:
                params_["data_nascimento"] = ""

            celular = str(request_["parameters"].get("numero_celular"))
            dddcel = celular[:2]
            numcel = celular[2:]
            telefone = str(request_["parameters"].get("numero_telefone"))
            dddtel = telefone[:2]
            numtel = telefone[2:]
            if telefone == "Não":
                params_['telefone'] = "9999999"
                params_['ddd_telefone'] = "11"
            else:
                params_['telefone'] = numtel
            params_['ddd_celular'] = dddcel
            params_['ddd_telefone'] = dddtel
            params_['celular'] = numcel
            params_['email'] = str(request_["parameters"].get("email"))
            params_['logradouro'] = str(request_["parameters"].get("logradouro"))

            nacionalidade_ = str(request_["parameters"].get("nacionalidade", "brasileiro")).lower()

            if nacionalidade_ == 'brasileiro':
                params_["nacionalidade"] = "BRASILEIRA"

            elif nacionalidade_ == 'brasileiro naturalizado':
                params_["nacionalidade"] = "NATURALIZADO"

            elif nacionalidade_ == 'estrangeiro':
                params_["nacionalidade"] = "ESTRANGEIRO"

            elif nacionalidade_ == 'brasileiro nascido no exterior':
                params_["nacionalidade"] = "BRASILEIRO_NASCIDO_EXTERIOR"

            params_['naturalidade'] = str(request_["parameters"].get("naturalidade"))

            params_["necessidade_veiculo_adaptado"] = "S" \
                if str(request_["parameters"].get("necessidade_veiculo_adaptado", "SIM")) == "SIM" else "N"

            params_['nome'] = str(request_["parameters"].get("nome"))
            params_['nome_mae'] = str(request_["parameters"].get("nome_mae"))
            params_['nome_pai'] = str(request_["parameters"].get("nome_pai"))

            params_['numero_carteira_militar'] = str(request_["parameters"].get("numero_carteira_militar", ""))
            params_['numero_documento'] = str(request_["parameters"].get("numero_documento"))

            params_['numero'] = str(request_["parameters"].get("numero"))

            params_['orgao_documento'] = str(request_["parameters"].get("orgao_documento"))

            params_["pretende_atividade_remunerada"] = "N" \
                if str(request_["parameters"].get("pretende_atividade_remunerada", "")).upper() == "" \
                else "S"

            params_['sexo'] = str(request_["parameters"].get("sexo", "")).upper()

            params_['teste_alfabetizacao'] = str(request_["parameters"].get("teste_alfabetizacao", "S"))
            params_['tipo_documento'] = "CARTEIRA_IDENTIDADE"
            params_['uf_documento'] = "SP"

            params_['num_RNE'] = str(request_["parameters"].get("num_RNE", ""))
            params_['orgao_RNE'] = str(request_["parameters"].get("orgao_RNE", ""))
            params_['uf_RNE'] = str(request_["parameters"].get("uf_RNE", ""))
            context_ = await Consumers.servGerarRenach(params_, request_["service"])

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        if context_ == {}:

            return {
                "text": "api_nok",
                "context": {}
            }

        else:

            context_tratado_: dict = {}
            context_tratado_ = splitDict("proc9038_", context_)

            cod_ = int(context_.get("codigo", 0))

            if cod_ == 0:

                retorno_ = {
                    'text': 'api_ok',
                    'context': context_tratado_
                }
            else:

                if cod_ == 374:
                    retorno_ = {
                        'text': 'api_nok',
                        'context': context_tratado_
                    }

                else:

                    retorno_ = {
                        'text': 'api_nok',
                        'context': context_tratado_
                    }

        retorno_["context"]["process"] = ""

        return retorno_
