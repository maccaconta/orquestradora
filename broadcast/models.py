from django.db import models


class WhatsTemplate(models.Model):
    """
             Name            : WhatsTemplate
            :class           : faz
            :create          : julho-2021
            description      : faz
    ____________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    template = models.TextField('template')
    type = models.CharField('tipo', max_length=16)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        verbose_name_plural = 'Templates'
        verbose_name = 'Template'

