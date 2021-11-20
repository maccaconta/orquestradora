from json import loads


class TemplateSerializer:

    @staticmethod
    async def template_serializer(data: dict) -> None:
        # print(data.template)
        return loads(data.template)

