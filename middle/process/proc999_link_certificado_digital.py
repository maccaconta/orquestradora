from middle.consumers.consumers import Consumers


class Proc999LinkCertificadoDigital(Consumers):

    @staticmethod
    def get_certificado_digitial(request_) -> dict:
        """
         name: proc_validar_cadastro
        :param request_: request
        :return: expression_list
        """
        _context = Consumers.fetch_poupinha_certificado_digital(request_)

        if _context == {}:
            return {
                "text": "download_notok",
                "context": {}
            }
        else:

            return {
                "text": "download_ok",
                "context": _context
            }