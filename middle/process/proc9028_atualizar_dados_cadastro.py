from api.utilities import splitDict
from middle.consumers.consumers import Consumers

class Proc9028AtualizarDadosCadastro(Consumers):

    async def get_atualizar_dados_cadastro(request_) -> dict:
        """
        name: get_atualizar_dados_cadastro
        :param request_: request
        :return: dict
        """
        params_: dict = {}
        context_: dict = {}
        return_: dict = {}
        
        try:
            orgao_documento = str(request_["parameters"]["proc9028_orgao_documento"]) if "proc9028_orgao_documento" in request_["parameters"] else str(request_["parameters"]["orgao_documento"])
            uf_documento = str(request_["parameters"]["proc9028_uf_documento"]) if "proc9028_uf_documento" in request_["parameters"] else str(request_["parameters"]["uf_documento"])
            
            params_["bairro"] =  str(request_["parameters"].get("bairro", ""))
            params_["cep"] =  str(request_["parameters"].get("cep", ""))
            params_["complemento"] =  str(request_["parameters"].get("complemento", ""))
            params_["cpf"] =  str(request_["parameters"].get("cpf", ""))
            params_["cpf_alteracao"] =  str(request_["parameters"].get("cpf_alteracao", ""))
            params_["data_nascimento"] =  str(request_["parameters"].get("data_nascimento", ""))
            params_["data_primeira_habilitacao"] =  str(request_["parameters"].get("data_primeira_habilitacao", ""))
            params_["endereco"] =  str(request_["parameters"].get("logradouro", ""))
            params_["municipio"] =  str(request_["parameters"].get("municipio", ""))
            params_["nome"] =  str(request_["parameters"].get("nome", ""))
            params_["nome_mae"] =  str(request_["parameters"].get("nome_mae", ""))
            params_["nome_pai"] =  str(request_["parameters"].get("proc9028_nome_pai", ""))
            params_["numero_documento"] =  str(request_["parameters"].get("proc9028_numero_documento", ""))
            params_["numero"] =  str(request_["parameters"].get("numero", ""))
            params_["numero_espelho"] =  str(request_["parameters"].get("proc9028_numero_espelho", ""))
            params_["orgao_documento"] =  orgao_documento
            params_["registro"] =  str(request_["parameters"].get("numero_registro", ""))
            params_["tipo_alteracao"] =  str(request_["parameters"].get("tipo_alteracao", ""))
            params_["uf_documento"] =  uf_documento

        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_atualizar_dados_cadastro(params_, request_["service"])


        if context_ == {}:
            return {
                "text": "api_nok",
                "context": {}
            }
        else:
            try:
                context_tratado_: dict = {}
                context_tratado_ = splitDict("proc9028_", context_)
                
                try:
                    cod_ = int(context_tratado_['proc9028_codigo'])
                    if cod_ == 0:
                        return_ = {
                            'text': 'api_ok',
                            'context': context_tratado_
                        }

                    else:
                        return_ = {
                            'text': 'api_nok',
                            'context': ""
                            }

                except Exception as e:
                    print("Falha na extração do codigo", e)
                    context_tratado_ = "proc9028"

            except Exception as e:
                print("Falha na atualização da matrix", e)
                return_ = {
                    'text': 'api_nok',
                    'context': context_tratado_
                }

        return_["context"]["process"] = ""

        return return_
