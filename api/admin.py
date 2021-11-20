from .models import (BulkClassifyResponse, Attendance,
                     Citizen, File, Routers,
                     Recipient, SetSystem,
                     Channel, Skill, ChannelSkill, Service, GuidePost, PostService)
from django.contrib import admin


@admin.register(BulkClassifyResponse)
class BulkAdmin(admin.ModelAdmin):
    list_display = ('id_bulk',
                    'session',
                    'question',
                    'answer',
                    'created_at',
                    'updated_at')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        'id_attendance',
        'cpf',
        'session',
        'intent',
        'channel',
        'confidance',
        'step',
        'longitude',
        'latitude',
        'protocol',
        'ip',
        'token',
        'id_node',
        'id_citizen',
        'created_at',
        'updated_at')


@admin.register(SetSystem)
class SetSystemAdmin(admin.ModelAdmin):
    list_display = (
        'id_attendance',
        'created_at',
        'updated_at')


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = (
        'id_citizen',
        'cpf',
        'email',
        'mobile',
        'client_id',
        'full_name',
        'client_token',
        'created_at',
        'updated_at')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'id_file',
        'id_attendance',
        'id_instruction',
        'dt_checking',
        'is_checking',
        'dt_checkout',
        'is_checkout',
        'file_name',
        'file_path',
        'file',
        'cpf',
        'pause',
        'created_at',
        'updated_at')


@admin.register(Routers)
class RoutersAdmin(admin.ModelAdmin):
    list_display = (
        'id_router',
        'id_recipient',
        'is_process',
        'is_link',
        'is_document',
        'process',
        'url',
        'documents',
        'created_at',
        'updated_at',
        'service')


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = (
        'id_recipient',
        'recipient',
        'email',
        'service',
        'path',
        'created_at',
        'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'url_serv_prod',
        'url_serv_homo',
        'url_auth_prod',
        'url_auth_homo',
        'client_secret',
        'client_id',
        'grant_type',
        'scope',
        'created_at',
        'updated_at')


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = (
        'channel',
        'code')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'skil_name',
        'assistant_apikey',
        'assistant_id',
        'assistant_url',
        'assistant_version',
        'created_at',
        'updated_at')


@admin.register(ChannelSkill)
class ChannelSkillAdmin(admin.ModelAdmin):
    list_display = (
        'channel',
        'id_skil',
        'step',
        'started'
    )

@admin.register(PostService)
class PostServicelAdmin(admin.ModelAdmin):
    list_display = (
        'id_post_service',
        'id_service',
        'id_guide_post',
        'description',
        'id_organ',
        'validator_ne',
        'validator_s',
        'validator_sa'
    )

@admin.register(GuidePost)
class GuidePostAdmin(admin.ModelAdmin):
    list_display = (
        'id_guide_post', 
        'id_post_guide', 
        'id_1',
        'id_8',
        'id_2', 
        'id_16', 
        'description',
        'address',
        'city'
    )
