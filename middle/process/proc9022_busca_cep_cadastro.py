from api.utilities import splitDict
from middle.consumers.consumers import Consumers

class Proc9022BuscaCepCadastro(Consumers):
    async def get_busca_cep_cadastro(request_) -> dict:
        """
         name: get_busca_cep_cadastro
        :param request_: request
        :return: dict
        """        
        params_: dict = {}
        context_: dict = {}
        return_: dict = {}

        try:
            params_["arquivos"] = str(request_["parameters"].get("arquivos", " "))
            params_["bairro"] = str(request_["parameters"].get("bairro", " "))
            params_["cep"] = str(request_["parameters"].get("cep", " "))
            params_["codigoCategoria"] = str(request_["parameters"].get("codigoCategoria", " "))
            params_["codigoMunicipioDenatran"] = str(request_["parameters"].get("codigoMunicipioDenatran", " "))
            params_["codigoUnidadeRetirada"] = str(request_["parameters"].get("codigoUnidadeRetirada", " "))
            params_["complemento"] = str(request_["parameters"].get("complemento", " "))
            params_["cpfCnpj"] = str(request_["parameters"].get("cpfCnpj", " "))
            params_["email"] = str(request_["parameters"].get("email", " "))
            params_["logradouro"] = str(request_["parameters"].get("logradouro", " "))
            params_["necessitaValidacao"] = str(request_["parameters"].get("necessitaValidacao", " "))
            params_["nomeProprietario"] = str(request_["parameters"].get("nomeProprietario", " "))
            params_["numeroEspelhoCrv"] = str(request_["parameters"].get("numeroEspelhoCrv", " "))
            params_["numeroLogradouro"] = str(request_["parameters"].get("numeroLogradouro", " "))
            params_["observacao"] = str(request_["parameters"].get("observacao", " "))
            params_["placa"] = str(request_["parameters"].get("placa", " "))
            params_["renavam"] = str(request_["parameters"].get("renavam", " "))
            params_["tipoDocumento"] = str(request_["parameters"].get("tipoDocumento", " "))
            params_["ufOrigemVeiculo"] = str(request_["parameters"].get("ufOrigemVeiculo", " "))
            params_["orgExpRg"] = str(request_["parameters"].get("orgExpRg", " "))
            params_["rg"] = str(request_["parameters"].get("rg", " "))
            params_["ufRg"] = str(request_["parameters"].get("ufRg", " "))

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)
        
        context_ = await Consumers.serv_busca_cep_cadastro(params_, request_["service"])
        
        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9022_",context_)
                try:
                    cod_ = int(context_tratado_['proc9022_codigo'])
                    if cod_ == 0:
                        return_ = {
                            'text': 'api_ok',
                            'context': context_tratado_
                        }
                    else:
                        return_ = {
                            'text': 'api_nok',
                            'context':""
                        }
                except Exception as e:
                    print("Falha na extração no codigo", e)
                    context_tratado_ = "proc9022"
            
            except Exception as e:
                print("Falha na atualização na matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }
        return return_
