from django.contrib import admin

from .models import WhatsTemplate
from django.contrib import admin


@admin.register(WhatsTemplate)
class WhatsTemplateAdmin(admin.ModelAdmin):
    list_display = ('template',
                    'created_at',
                    'updated_at')
