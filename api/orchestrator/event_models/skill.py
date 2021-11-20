from api.models import ChannelSkill
from api.models import Skill
from decouple import config

class EventModelSkillMixin(object):

    def getSkill(self, channel) -> list:
        """
         getSkill: retorna as skills por canal
         Descrição: Se a variável de ambiente ASSISTANT_CREDENTIALS_DB, definida no arquivo .env
                     for True, as credenciais virão do banco de dados, caso contrário, elas deverão
                     ser definidas no próprio arquivo .env.
        :param channel (whatsapp, webcliente etc)
        :return: skills dicr
        """

        lst_skills: dict = {}

        #
        #

        if config('ASSISTANT_CREDENTIALS_DB', cast=bool):

            try:

                skill_ = Skill.objects.all().prefetch_related('skills')
                channelskil_ = ChannelSkill.objects.filter(channel=channel).order_by('step')

                for i, skill_ in enumerate(channelskil_):
                    lst_skills[i] = skill_.id_skil

                return lst_skills

            except:
                return []
        else:

            i_: int = 0

            lst_skills[0] = {
                'assistent_apikey': config('ASSISTANT_APIKEY'),
                'assistent_id': config('ASSISTANT_ID'),
                'assistent_url': config('ASSISTANT_URL'),
                'assistent_version': config('ASSISTANT_VERSION')
            }

            return lst_skills




