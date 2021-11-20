from api.models import SetSystem as Files
from datetime import datetime
from django.conf import settings

from django.core.files import File
from django.db.models import F


class EventModelDocuments:
    def saveDocument(self, id, recipient, file) -> bool:

        """
        ---------------------------------------------------
        funcSaveDocument salva o documento na base de dados

        :param self:
        :param recipient: dados do router e do cidadão
        :param file:
        :return: bool
        ---------------------------------------------------
        """

        file_name_ = recipient['cpf'] + " - " + datetime.now().strftime("%Y%d%Y%m%M%S") + '.pdf'
        repository_ = settings.REPOSITORY

        if self.saveFileInRepository(repository_, file_name_, file):

            file_ = Files()
            file_.id_attendance = id
            file_.file_name = file_name_
            file_.file = repository_ + file_name_
            file_.cpf = recipient['cpf']
            file_.save()

            # self.message['question'] = 'uploaded'
            # self.routers["is_upload"] = False

            return True
        else:
            # todo: gravar log
            # self.message['question'] = 'not uploaded'
            return False

    @staticmethod
    def saveFileInRepository(self, repository: str, file_name: str, file: object) -> bool:

        """
        ---------------------------------------------------
        saveFileInRepository: salva temporarioamente no repositório os documentos
         enviados pelo chatbot

        :param file_name: Nome do arquivo
        :param repository: Nome o repositório
        :param file: Objeto file
        :return:True para sucesso na gravação
        ---------------------------------------------------
        """

        try:
            with open(repository + file_name, 'w') as f:
                file_ = File(f)
                file_.write(str(file))
            file_.close()

            return True
        except:
            return False