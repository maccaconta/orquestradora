from middle.consumers.consumers import Consumers
from common.utils import Formatted


class Proc0008Agendamentos(Consumers):

    async def get_agendamentos(request_) -> dict:
        """
         name: get_agendamentos
        :param request_: request
        :return: dict
        """
        context_: dict = {}
        params_: dict = {}
        retorno_ = {
            "text": "",
            "context": context_
        }

        if request_["parameters"].get("cpf"):
            cpf_ = Formatted(str(request_["parameters"].get("cpf")))
        else:
            cpf_ = request_["parameters"].get("proc0002_cpf")


        try:

            params_["idOrgao"] = str(request_["parameters"].get("idOrgao", ""))
            params_["idLocal"] = str(request_["parameters"].get("id1", ""))
            params_["idServico"] = str(request_["parameters"].get("idServico", ""))
            params_["horario"] = str(request_["parameters"].get("horario_tratado", ""))
            params_["sa_id_cidadao"] = str(request_["parameters"].get("proc0002_Id", "00000000-0000-0000-0000-000000000000"))
            params_["sa_id_atendimento"] = str(request_["parameters"].get("sa_id_atendimento", ""))
            params_["ipOrigemAgendamento"] = str(request_["parameters"].get("ipOrigemAgendamento", ""))
            params_["canalEvento"] = "AVI"
            params_["cidadao"] = {}
            params_["cidadao"]["nome"] = str(request_["parameters"].get("proc0002_Nome", ""))
            params_["cidadao"]["cpf"] = cpf_
            params_["cidadao"]["rg"] = str(request_["parameters"].get("rg", ""))
            params_["cidadao"]["dddCelular"] = str(request_["parameters"].get("proc0002_CelularDdd", ""))
            params_["cidadao"]["celular"] = str(request_["parameters"].get("proc0002_Celular", ""))
            params_["cidadao"]["dddTelefone"] = str(request_["parameters"].get("dddTelefone", ""))
            params_["cidadao"]["telefone"] = str(request_["parameters"].get("telefone", ""))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        try:

            context_ = await Consumers.serv_agendamentos(params_, request_["service"])

        except Exception as e:
            print("Erro no Context", e)

        if type(context_) is str:

            retorno_ = {
                "text": "api_erro",
                "context": {
                    'proc0008_msg': context_,
                    'process': ""
                    }
            }
        elif type(context_) is dict:

            if context_ == {}:
                retorno_ = {
                    "text": "api_nok",
                    "context": {'proc0008_msg': context_}
                }

            else:

                retorno_ = {
                    "text": "api_ok",
                    "context": context_
                }

        return retorno_
