from api.models import GuidePost
from asgiref.sync import sync_to_async
from api.utilities import fetchGET


class ServicePostosId:

    @staticmethod
    async def serv_postos_id(params, service) -> dict:
        """
        nome: serv_postos_poupatempo
        :return: ...
        """

        headers_: dict = {}
        return_: dict = {}

        try:
            post = await sync_to_async(GuidePost.objects.get)(description=params['description'])
            post_id = post.__dict__["id_" + str(params['organ_id'])]
        except Exception as e:
            msg = "Falha ao buscar dados do banco"
            print(msg, e)
            return_ = {
                "code": 500,
                "message": msg
            }

            return return_

        try:
            url_ = service.get("url") + "/v1/servicos/orgaos/" + str(params["organ_id"]) \
                + "/locais/" + str(post_id)

            headers_ = {
                'Authorization': "Bearer " + service.get("token"),
                'Cache-Control': "no-cache",
                'Content-Type': "application/json",
                'Accept': "*/*",
                'Connection': "keep-alive"
            }

            print("URL da requisição:", url_)

            retorno_ = await fetchGET(url_, headers_)
            print("Retorno da API:", retorno_)

        except Exception as e:
            print("Retorno da API Error: ", e)
            retorno_ = {}

        return_ = {
            "idPostoGuia": post.id_post_guide,
            "id1": post.id_1,
            "id8": post.id_8,
            "id2": post.id_2,
            "id16": post.id_16,
            "descricao": post.description,
            "endereco": post.address,
            "cidade": post.city,
            "service": retorno_,
            "code": 0,
            "posto_id": post_id
            
        }

        return return_

def service_as_json(s):
    return{
        "id": s.id_service,
        "descrição": s.description,
        "idOrgan": s.id_organ,
        "ne": s.validator_ne,
        "s": s.validator_s,
        "sa": s.validator_sa

    }
