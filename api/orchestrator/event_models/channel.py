from api.models import Channel
from decouple import config


class EventModelChannelMixin(object):

    def getChannel(self, channel_: str) -> str:
        """
        key_generator: retorna retorna uma chave de identificação baseado na tabela (channel=canal)
        :param channel (whatsapp, webcliente etc)
        :return: id do atendimento
        """

        for _ in range(2):

            try:
                data_ = Channel.objects.get(channel=channel_)

                return data_.code

            except Exception as e:

                channel_ = config('CANAL')

        return data_.code