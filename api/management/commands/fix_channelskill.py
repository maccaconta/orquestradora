from django.core.management.base import BaseCommand
from api.models import ChannelSkill, Skill


class Command(BaseCommand):
    help = 'Valor default da configuração do ChannelSkill'

    def handle(self, **options):
        self.stdout.write('Deletando dados de ChannelSkill')
        ChannelSkill.objects.all().delete()
        
        
        self.stdout.write('Criando dados Default do ChannelSkill')

        # whatsapp
        # ---------

        ChannelSkill.objects.get_or_create(
            id_skil=Skill(id=1),
            channel='whatsapp',
            step=2,
            started=True)

        ChannelSkill.objects.create(
            id_skil=Skill(id=2),
            channel='whatsapp',
            step=1,
            started=True)

        ChannelSkill.objects.create(
            id_skil=Skill(id=1),
            channel='webclient',
            step=1,
            started=True)

        ChannelSkill.objects.create(
            id_skil=Skill(id=2),
            channel='webclient',
            step=1,
            started=True)

