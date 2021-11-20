from middle.consumers.consumers import Consumers
from common.utils import Formatted


class Proc0014DataFeriado(Consumers):

    async def get_data_feriado(request_) -> dict:
        """
         name: get_data_feriado
        :param request_: request
        :return: dict
        """

        params_: dict = {}
        context_: dict = {}
        treatment_: dict = {}
        data_watson: str = ""

        try:

            data_watson = str(request_["parameters"].get("data", ""))

            if data_watson == "Troca posto" or data_watson == "Cancelar" or data_watson == "Alterar CPF":
                return {
                    "text": "api_ok",
                    "context": {
                        'process': ""
                    }
                }
            else:
                data = Formatted(str(request_["parameters"].get("data", "")))

            params_["data"] = data[-4:] + data[2:4] + data[:2]
            params_["posto_id"] = str(request_["parameters"].get("posto_id", ""))
          
        except Exception as e:
            print("Erro na criação dos parâmetros na PROC", e)

        context_ = await Consumers.serv_data_feriado(params_, request_["service"])
       
        if context_ == {}:
            return {
                "text": "api_ok",
                "context": {
                    'process': ""
                }
            }

        if "Not Found" in context_:
            
            return {
                'text': 'api_ok',
                'context': {
                    'process': ""
                }
            }
        else:
            treatment_ = {
                "proc0014_feriado": context_[0]["DS_TITULO"],
                "proc0014_descrição": context_[0]["DS_DESCRICAO"],
                "process": ""
               
            }
            return {
                'text': 'api_erro',
                'context': treatment_

            }
      
