from api.models import Service
from asgiref.sync import sync_to_async


def assembly(datas: dict):
    for data in datas:
        datas[str(data)] = str(datas[str(data)])


async def search_url(service: str):
    data = await sync_to_async(Service.objects.get)(service=service)
    return data
    
def assembly(datas: dict):
    for data in datas:
        datas[str(data)] = str(datas[str(data)])
