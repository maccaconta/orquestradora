from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(BaseCommand):
    help = 'Valor default da configuração do ChannelSkill'

    def handle(self, **options):
        self.stdout.write('Deletando dados de User')
        User.objects.all().delete()

        self.stdout.write('Criando dados Default do User')
        User.objects.create_superuser(
            username='admin',
            email='',
            password='magna123')