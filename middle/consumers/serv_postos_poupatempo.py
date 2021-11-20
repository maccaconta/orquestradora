from api.models import GuidePost
from asgiref.sync import sync_to_async
from api.utilities import fetchGET


class ServicePostosPoupatempo:

    @staticmethod
    async def serv_postos_poupatempo(params, service) -> dict:
        """
        nome: serv_postos_poupatempo
        :return: ...
        """

        return_: dict = {}

        try:
            posts = await get_posts(params["city"])

        except Exception as e:

            msg = "Falha ao buscar dados do banco"
            print(msg, e)
            return_ = {
                "code": 500,
                "message": msg
            }

            return return_

        posts_json = []

        url = service.get("url")
        token = service.get("token")
        organ_id = params.get("organ_id")
        service_id = str(params.get("service_id"))

        for post in posts:
            p_ = post.__dict__
            post_id = p_["id_" + str(organ_id)]

            try:
                url_ = str(url) + "/v1/servicos/orgaos/" + str(organ_id) \
                    + "/locais/" + str(post_id)

                headers_ = {
                    'Authorization': "Bearer " + str(token),
                    'Cache-Control': "no-cache",
                    'Content-Type': "application/json",
                    'Accept': "*/*",
                    'Connection': "keep-alive"
                }

                print("URL da requisição:", url_)

                retorno_ = await fetchGET(url_, headers_)
                services = retorno_
                print("Retorno da API:", retorno_)

            except Exception as e:
                print("Retorno da API Error: ", e)
                retorno_ = {}

            services_list = []
            if "Parâmetro local não foi informado corretamente" in retorno_:
                return {'code': 500
                        }

            else:
                for service in services:
                    if (service_id == str(service['identificador'])):
                        services_list.append(service)

                if len(services_list) > 0:
                    p_["service"] = services_list
                    posts_json.append(p_)

        if posts == []:
            msg = "Falha ao buscar dados do banco"
            return_ = {
                "code": 500,
                "message": msg
            }
        else:
            return_ = {
                "post": posts_json,
                "code": 0
            }

        return return_


@sync_to_async
def get_posts(city):
    return list(GuidePost.objects.all().filter(city=city))
