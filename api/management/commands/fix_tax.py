from django.core.management.base import BaseCommand
from api.models import TaxPayment


class Command(BaseCommand):

    def handle(self, **options):
        self.stdout.write('Deletando dados de TaxPayment')
        TaxPayment.objects.all().delete()

        self.stdout.write('Criando dados Default do TaxPayment')

        TaxPayment.objects.create(
                                tax_type = "cnh_definitiva",
                                tax_name = "Taxa bancaria CNH Definitva",
                                tax_value = 96.00)

        TaxPayment.objects.create(
                                tax_type = "cnh_inicial",
                                tax_name = "Taxa bancaria Primeira CNH",
                                tax_value = 150.99)

        TaxPayment.objects.create(
                                tax_type = "cnh_segunda_via",
                                tax_name = "Taxa bancaria Segunda Via CNH",
                                tax_value = 15.99)
