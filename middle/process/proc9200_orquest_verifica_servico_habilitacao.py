from middle.consumers.consumers import Consumers


class Proc9200OrchestVerificaServicoHabilitacao(Consumers):

    async def getServicoHabilitacao(request) -> dict:
        """
        name: get_endereco_para_entrega
        :param request_: request
        :return: dict
        """

        verifica_servico_:str = ""

        try:
            verifica_servico_ = str(request["parameters"].get("verifica_servico"))

            print("Retorno Api 200: ", verifica_servico_)

        except:
            verifica_servico_ = "cnh_primeira_habilitacao"

        return {
            "text": verifica_servico_,
            "context": {"process": ""}
        }