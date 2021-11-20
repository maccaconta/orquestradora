from api.utilities import splitDict
from middle.consumers.consumers import Consumers


class Proc9008AgendamentoMedicoCapitalRegiao(Consumers):

    async def get_agendamento_medico_capital(request_) -> dict:
        """
        name: get_agendamento_medico_capital
        :param request_: request
        :return: dict
        """

        context_: dict = {}
        retorno_: dict = {}
        params_: dict = {}

        try:
            params_["cpf_cidadao"] = int(request_["parameters"].get("cpf", ""))
            params_["tipo_exame"] = str(request_["parameters"].get("tipo_exame", ""))
            params_["usuario"] = request_["service"].get("canal").upper()

            params_["is_portador_necessidades_especiais"] = True \
                if str(request_["parameters"].get("is_portador_necessidades_especiais", "SIM")).upper() == "SIM" \
                else False

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_agendamento_medico_capital(params_, request_["service"])

        if context_ != {}:

            context_tratado_: dict = {}
            context_tratado_ = splitDict("proc9008_", context_)

            try:
                context_tratado_['proc9008_mensagem'] = context_['proc9008_mensagem'].lower()
            except:
                pass

            cod_ = int(context_tratado_.get("proc9008_codigo", 0))

            if cod_ == 400:  # Cadastro do Cidadão não está atualizado

                retorno_ = {
                    'text': 'api_erro',
                    'context': context_tratado_
                }

            elif cod_ == 0:  # Sucesso

                context_tratado_["proc9008_regioes"] = " "

                texto_ = ""

                for i in range(len(context_["regioes_medico"])):

                    long_id_ = ""
                    nome_ = ""

                    for context_key_, value_val_ in context_["regioes_medico"][i].items():

                        if context_key_ == "long_id":
                            long_id_ = str(value_val_)

                        if context_key_ == "nome":
                            nome_ = value_val_

                    texto_ += " " + long_id_ + ". " + nome_ + "  "

                context_tratado_["proc9008_regioes"] = texto_

                retorno_ = {
                    'text': 'api_ok',
                    'context': context_tratado_
                }
            else:
                retorno_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }

        else:

            retorno_ = {
                'text': 'api_nok',
                'context': {}
            }

        retorno_["context"]["process"] = ""

        return retorno_
