from middle.consumers.consumers import Consumers


class Proc9043EncontrarProcessos(Consumers):

    async def get_encontrar_processos(request_) -> dict:
        """
         name: get_encontrar_processos
        :param request_: request
        :return: dict
        """
        
        params_: dict = {}
        context_: dict = {}
        return_: dict = {}
        try:
            params_["registro"] = str(request_["parameters"].get("numero_registro", ""))
            params_["cpf"] = str(request_["parameters"].get("cpf", ""))
            
        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_encontrar_processos(params_, request_["service"])    

        if context_ == {} or not context_:
            return {
                "text": "api_nok",
                "context": {}
            }            
        else:
            try:
                context_tratado_: dict = {}
                maior: int = 0
                obj: dict = {}
                portaria: dict = []
                context_tratado_["penalidade_cumprimento"] = context_["cumprimento"]["penalidade_cumprimento"]
                context_tratado_["data_inicio_cumprimento"] = context_["cumprimento"]["data_inicio_cumprimento"]
                context_tratado_["data_fim_cumprimento"] = context_["cumprimento"]["data_fim_cumprimento"]
                if 'portarias' in context_:
    
                    for i, context in enumerate(context_['portarias']):
                        
                        context_tratado_[f'processo_{i+1}'] = f'Processo Administrativo: {context["numero_processo"]}/{context["ano_processo"]}'
                        context_tratado_[f'status_portaria_{i+1}'] = f'Status do Processo: {context["status_portaria"]}'
                        context_tratado_[f'pena_{i+1}'] = f'Penalidade: {context["pena"]}'
                        context_tratado_[f'portarias_{i+1}']= context["portaria"]
                        obj["portaria"] = int(context['portaria'])
                        obj["numero_processo"] = int(context['numero_processo'])
                        obj["ano_processo"] = int(context['ano_processo'])
                        obj["renuncia"] = bool(context['renuncia'])
                        portaria.append(obj)
                        obj = {}
                        value = int(context["pena"].partition("mes(es)")[0])
                        if value > maior:
                            maior = value
                context_tratado_["total_pena"] = maior
                context_tratado_["portarias"] = portaria
                if 'requerimento' in context_:
                    datas = context_['requerimento'].values()

                    for i, data in enumerate(datas):
                        context_tratado_[f'paragrafo_{i+1}'] = f'{str(data)}'

                # else:
                #     return_ = {
                #         'text': 'api_erro',
                #         'context': context_
                #     }

                return_ = {
                            'text': 'api_ok',
                            'context': context_tratado_
                        }
                                
            except Exception as e:
                print("Falha na criação do context tratado", e)
                return_ = {
                    'text': 'api_nok',
                    'context': {}
                }

        return_["context"]["process"] = ""
        return return_
