from api.models import BulkClassifyResponse


class EventModelBulk:

    @staticmethod
    def saveBulk(_bulk):
        """
        -----------------------------------------
        saveBulk: salva bulk classifc response na talela BulkClassifcResponse
        :param _bulk:
        :return:
        -----------------------------------------
        """

        try:
            options_or_text: list = []

            if _bulk['answer']['data'][0]['type'] == 'text':
                options_or_text.append(_bulk['answer']['data'][0]['text'])
            elif _bulk['answer']['data'][0]['type'] == 'option':
                for data in _bulk['answer']['data'][0]['option']['select']['options']:
                    options_or_text.append(data["label"])
                options_or_text.append(f"texto do balão: {_bulk['answer']['data'][0]['option']['select']['title']}")
            elif _bulk['answer']['data'][0]['type'] == 'link':
                options_or_text.append(_bulk['answer']['data'][0]['link'])
                options_or_text.append(f"texto do balão: {_bulk['answer']['data'][0]['title']}")
            elif _bulk['answer']['data'][0]['type'] == 'upload':
                options_or_text.append("upload de arquivo")

            BulkClassifyResponse.objects.create(session=_bulk.get('session'),
                                                question=_bulk.get('question', ''),
                                                answer=options_or_text)
            return True
        except:
            return False

    def deleteBulk(self):
        pass
