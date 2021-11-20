class ServicePoupinhaLinkCertificadoDigital:

    @staticmethod
    def fetch_poupinha_certificado_digital(request) -> dict:
        retorno_: dict = {

            'cpf': '999999999999',
            'nome': 'jose',
            'tipo_documento': 'Certificado Digital',
            'download': "https://cdn.positus.global/production/resources/samples/document.pdf"
        }

        return retorno_
