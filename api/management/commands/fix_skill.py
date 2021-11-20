from django.core.management.base import BaseCommand
from api.models import Skill


class Command(BaseCommand):
    help = 'Valor default da configuração da tabela Skill'

    def handle(self, **options):
        self.stdout.write('Deletando dados de Skill')
        Skill.objects.all().delete()
        
        self.stdout.write('Criando dados default da tabela Skill')
    

        Skill.objects.create(
            id=1,
            skil_name='detran',
            assistant_id='5302a3fd-c041-4576-b5cb-b5ec2ce416bf',
            assistant_apikey="6ubZYkwcy85tX-HWmqY85lBrfk-xFof8ICL7yVqyDwAo",
            assistant_url='https://api.us-south.assistant.watson.cloud.ibm.com/instances/f60c9f83-6f5c-43ea-93a6-c065430dc143',
            assistant_version='2020-06-19')

        Skill.objects.create(
            id=2,
            skil_name='poupinha',
            assistant_id='5302a3fd-c041-4576-b5cb-b5ec2ce416bf',
            assistant_apikey="6ubZYkwcy85tX-HWmqY85lBrfk-xFof8ICL7yVqyDwAo",
            assistant_url='https://api.us-south.assistant.watson.cloud.ibm.com/instances/f60c9f83-6f5c-43ea-93a6-c065430dc143',
            assistant_version='2020-06-19')
