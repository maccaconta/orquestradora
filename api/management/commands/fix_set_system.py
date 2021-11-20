from django.core.management.base import BaseCommand
from api.models import SetSystem


class Command(BaseCommand):
    """
             Name            : Command
            :param          : BaseCommand
            :create         : junho-2021
            description     : faz...
    ____________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    help = 'Valor default da configuração do Setsystem'

    def handle(self, **options):
        """
        nome: handle
        :param options: str
        :return:
        """
        self.stdout.write('Deletando dados de SetSystem')
        SetSystem.objects.all().delete()

        self.stdout.write('Criando dados Default do Setsystem')

        SetSystem.objects.create(id_attendance=0)

