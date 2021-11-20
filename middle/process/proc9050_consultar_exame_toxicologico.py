from middle.consumers.consumers import Consumers


class Proc9050ConsultaExameToxicologico(Consumers):

    async def getConsultaExameToxicologico(request_) -> dict:
        """
         name: get Exame Toxicologico
        :param request_: request
        :return: dict
        """

        _context = await Consumers.servConsultaExameToxicologico(request_)

        if _context == {}:
            return {
                "text": "api_nok",
                "context": {}
            }
        else:

            return {
                "text": "api_ok",
                "context": _context
            }