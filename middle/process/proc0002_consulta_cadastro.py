from middle.consumers.consumers import Consumers
from api.utilities import splitDict
from common.utils import mascara_email, mascara_telefone
from common.utils import Formatted
from common.cpf_cnpj_validator import ValidaCpfCnpj

validator: ValidaCpfCnpj = ValidaCpfCnpj()


class Proc0002ConsultaCadastro(Consumers):

    async def get_consulta_cadastro(request_) -> dict:
        """
         name: get_consulta_cadastro
        :param request_: request
        :return: dict
        """
        context_tratado_: dict = {}
        treatment_: dict = {}
        context_name: str = ""
        context_ = {}
        retorno_ = None

        try:
            retorno_ = await Consumers.serv_consulta_cadastro(request_)
        except Exception as e:
            print(e)

        print("RETORNO WebService", retorno_)

        if type(retorno_) is str:

            context_ = {}

            if "404" in retorno_:
                context_['code'] = 404
            else:
                context_['code'] = 400

        else:

            context_ = retorno_

        if "Mensagem" in context_ and "Nenhum registro encontrado" in context_["Mensagem"]:
            cpf_ = Formatted(str(request_["parameters"].get("cpf")))
            validator.get_cpf_cnpj(cpf_)
            context_["Mensagem"] = "Não encontramos seu CPF em nosso cadastro."

            if validator.valida():
                
                context_['cpf'] = cpf_
                return {
                    "text": "api_erro",
                    "context": {
                        "msg": context_['Mensagem'],
                        "cpf": context_['cpf'],
                        "process": ""
                    }
                }
                
        elif 'code' in context_ and context_['code'] == 500:
            context_['process'] = ''
            return {
                "text": "api_erro",
                "context": context_
            }

        elif 'code' in context_ and context_['code'] == 400:
            context_['process'] = ''
            return {
                "text": "api_nok",
                "context": context_
            }

        else:

            try:

                if context_[0]["PortalPPT"]:
                    context_name = "PortalPPT"

                elif context_[0]["BalcaoMP"]:
                    context_name = "BalcaoMP"

                elif context_[0]["AgendaSP"]:
                    context_name = "AgendaSP"

                elif context_[0]["BalcaoDetran"]:
                    context_name = "BalcaoDetran"

                elif context_[0]["BalcaoIIRGD"]:
                    context_name = "BalcaoIIRGD"

                celular_ddd_value: str = ""
                celular_value: str = ""
                nascimento_value: str = ""

                if len(context_[0][context_name]["Telefones"]) > 0:
                    for i in range(len(context_[0][context_name]["Telefones"])):
                        if 'Celular' == context_[0][context_name]["Telefones"][i]['Tipo']:
                            celular_value = context_[0][context_name]["Telefones"][i]["Numero"]
                            celular_ddd_value = context_[0][context_name]["Telefones"][i]["DDD"]
                        else:
                            celular_value = ""
                            celular_ddd_value = ""
            
                if "Enderecos" in context_[0][context_name] and context_[0][context_name]["Enderecos"]:
                    municipio_value = context_[0][context_name]["Enderecos"]["Municipio"]
                else:
                    municipio_value = context_[0][context_name]["Municipio"]
                if 'Nascimento' in context_[0][context_name] and context_[0][context_name]["Nascimento"] != None:
                    nascimento_value = context_[0][context_name]["Nascimento"][8:10] + "/" + context_[0][context_name]["Nascimento"][5:7] + "/" + context_[0][context_name]["Nascimento"][:4]

                else:
                    nascimento_value = ""

                treatment_ = {
                    "Id": context_[0].get("Id", ""),
                    "cpf": context_[0][context_name].get("CPF", ""),
                    "Nome": context_[0][context_name].get("Nome", ""),
                    "RG": context_[0][context_name].get("RG", ""),
                    "digito": context_[0][context_name].get("DigitoRG", ""),
                    "Email": context_[0][context_name].get("Email", ""),
                    "Municipio": municipio_value,
                    "CelularDdd": celular_ddd_value,
                    "Celular": celular_value,
                    "DataNascimento": nascimento_value,
                    "Cep": context_[0][context_name].get("CEP", "")
                }

            except Exception as e:
                print("Value errors ", e)

                return {
                    "text": "api_erro",
                    "context": context_['Message']
                }

            context_tratado_ = splitDict("proc0002_", treatment_)
            context_tratado_['process'] = ''
            context_tratado_['canal'] = request_["service"]["canal"]
            context_tratado_['cpf'] = context_tratado_['proc0002_cpf']
            context_tratado_['cont_erros'] = int(0)

            if context_tratado_['proc0002_Municipio'] == "":
                context_tratado_['proc0002_Municipio'] = None
            
            if context_tratado_['proc0002_Celular'] != "":
                context_tratado_['telefone_mascara'] = mascara_telefone(context_tratado_['proc0002_Celular'])
            else:
                context_tratado_['telefone_mascara'] = ""

            if context_tratado_['proc0002_Email'] != "":
                context_tratado_['email_mascara'] = mascara_email(context_tratado_['proc0002_Email'])
            else:
                context_tratado_['email_mascara'] = ""
           
            if context_tratado_["proc0002_DataNascimento"] != str(request_["parameters"]["data_nascimento"]):
                cont_erros = int(request_["context"].get("cont_erros", 0))
                cont_erros += 1
                return {
                    "text": "api_erro",
                    "context": {
                        "msg": "Data de Nascimento não confere",
                        "cont_erros": cont_erros,
                        "process": ""
                    }
                }
            
            return {
                "text": "api_ok",
                "context": context_tratado_
            }
