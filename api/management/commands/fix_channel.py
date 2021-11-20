from django.core.management.base import BaseCommand
from api.models import Channel


class Command(BaseCommand):
    help = 'Valor default da configuração do tabela Channel (Canal)'

    def handle(self, **options):
        self.stdout.write('Deletando dados de Channel')
        Channel.objects.all().delete()

        self.stdout.write('Criando cliente whatsapp na tabela de canais')
        Channel.objects.create( channel="whatsapp",
                                code="001")

        self.stdout.write('Criando cliente webclient_detran na tabela de canais')
        Channel.objects.create( channel="webclient_detran",
                                code="002")

        self.stdout.write('Criando cliente telegram na tabela de canais')
        Channel.objects.create( channel="telegram",
                                code="003")

        self.stdout.write('Criando cliente webclient_poupinha na tabela de canais')
        Channel.objects.create(channel="webclient_poupatempo",
                                code="004")

