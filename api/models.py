from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from common.base_model import BaseModel

repository_ = settings.REPOSITORY
path_ = FileSystemStorage(location=repository_)


class BulkClassifyResponse(BaseModel):
    """"
             Name            : BulkClassifyResponse
            :class           : Class BulkClassifyResponse
            :create          : junho-2021
            description      : Models, inner numbers, text and json
    ____________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    id_bulk = models.IntegerField(primary_key=True)
    session = models.TextField('sessao', blank=True, default='')
    question = models.TextField('pergunta_usr', default='', blank=True)
    answer = models.TextField('resposta_watson', default='', blank=True)


class Attendance(BaseModel):
    """
    Classe Attendance
    Armazena informações do atendimentos
    """
    """"
             Name            : Attendance
            :class           : Class Attendance
            :create          : junho-2021
            description      : Models, inner numbers, string field, text and decimals 
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    id_attendance = models.CharField('id_atendimento', max_length=32, default='')
    cpf = models.CharField(max_length=11)
    session = models.TextField('sessao', blank=True, default='')
    intent = models.TextField('intencao', default='', blank=True)
    confidance = models.DecimalField('grau_confianca_intencao', max_digits=16, decimal_places=2, default=0)
    source = models.CharField('fonte', max_length=32, default='')  # TODO: Retirar apos implementar channel
    channel = models.CharField('canal', max_length=32, default='')  # webclient, whatsapp, poupinha, telegram
    id_node = models.TextField('id_no', default='', blank=True)
    step = models.CharField('status', max_length=15, default='opened')
    longitude = models.DecimalField(max_digits=22, decimal_places=16, default=0)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, default=0)
    protocol = models.TextField('protocolo', default='', blank=True)  # todo: sequencial inteiro
    ip = models.CharField(max_length=15)
    token = models.CharField(max_length=64, blank=True, default='')
    id_citizen = models.IntegerField('id_cidadao', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'atendimentos'
        verbose_name = 'atendimento'


class SetSystem(BaseModel):
    """"
             Name            : SetSystem
            :class           : Class SetSystem
            :create          : junho-2021
            :Models          : inner numbers
            description      : faz...
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    id_attendance = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'config_sistema'
        verbose_name = 'config_sistema'


class Citizen(BaseModel):
    """"
             Name            : Citizen
            :class           : Class Citizen
            :create          : junho-2021
            :Models          : inner numbers, string field, text and email
            description     : Stores "citizen" information
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    id_citizen = models.IntegerField(primary_key=True)
    cpf = models.CharField(max_length=11)
    full_name = models.TextField('nome_completo', default='', blank=True)
    email = models.EmailField('e-mail', default='', blank=True)
    nickname = models.TextField(default='', blank=True)
    mobile = models.TextField('celular', default='', blank=True)
    client_id = models.CharField(max_length=128, default=0)
    client_token = models.TextField(default='', blank=True)

    class Meta:
        verbose_name_plural = 'cidadaos'
        verbose_name = 'cidadao'


class File(BaseModel):
    """"
             Name            : File
            :class           : Class File
            :create          : junho-2021
            :Models          : auto complete, integers, date, time, boll, text,
                              absolute file system path, file upload field
            description      : faz...
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    id_file = models.BigAutoField(primary_key=True)
    id_attendance = models.IntegerField('id_atendimnento', default=0)
    id_instruction = models.IntegerField('id_instrução', default=0)
    dt_checking = models.DateTimeField('dt_checking', auto_now_add=True)
    is_checking = models.BooleanField(default=True)
    dt_checkout = models.DateTimeField(null=True, blank=True)
    is_checkout = models.BooleanField(default=False)
    pause = models.BooleanField(default=True)
    file_name = models.TextField('nm_arquivo', default='', blank=True)
    file_path = models.FilePathField('url_arquivo', default=path_)
    file = models.FileField('arquivo', storage=path_, null=True, blank=True)
    cpf = models.CharField(max_length=11)

    class Meta:
        verbose_name_plural = 'arquivos'
        verbose_name = 'arquivo'


# class ProcessCall(BaseModel):
#     process = models.TextField('processo', default='', blank=True)
#     channel = models.CharField('canal', max_length=10, default='')


class Routers(BaseModel):
    """"
             Name            : Routers
            :class           : Class Routers
            :create          : junho-2021
            :Models          : auto complete, integers, boll and text
            description      : faz...
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    id_router = models.BigAutoField(primary_key=True)
    id_recipient = models.IntegerField(default=1)
    is_process = models.BooleanField('eprocesso', default=True)
    is_link = models.BooleanField('elink', default=False)
    is_document = models.BooleanField('edocumento', default=False)
    process = models.TextField('processo', default='', blank=True)
    url = models.TextField(default='', blank=True)
    service = models.CharField('fonte', max_length=64, default='')
    documents = models.TextField('documentos', default='', blank=True)

    class Meta:
        verbose_name_plural = 'rotas'
        verbose_name = 'rota'


class Recipient(BaseModel):
    """
             Name            : Recipient
            :class           : Classe Recipient
            :create          : junho-2021
            :Models          : auto complete, text and email
            description      : faz...
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    id_recipient = models.BigAutoField(primary_key=True)
    recipient = models.TextField(default='', blank=True)
    email = models.EmailField('e-mail', default='', blank=True)
    service = models.TextField('service', default='', blank=True)
    path = models.TextField('path', default='', blank=True)


class Service(BaseModel):
    """
    Classe Service
    Estabelece path dos serviços Detran

    """
    service = models.CharField('servico', max_length=128, default='')
    url_serv_prod = models.CharField('url_prod', max_length=128, default='', null=True, blank=True)
    url_serv_homo = models.CharField('url_homo', max_length=128, default='', null=True, blank=True)
    url_auth_prod = models.CharField('url_auth', max_length=128, default='', null=True, blank=True)
    url_auth_homo = models.CharField('url_auth', max_length=128, default='', null=True, blank=True)
    client_secret = models.CharField('client_secret', max_length=64, default='', null=True, blank=True)
    client_id = models.CharField('client_id', max_length=64, default='', null=True, blank=True)
    grant_type = models.CharField('grant_type', max_length=64, default='', null=True, blank=True)
    scope = models.CharField('scope', max_length=256, default='', null=True, blank=True)


class Channel(BaseModel):
    """
    Classe Channel (Canais)
    Estabelece os canais no modelo base.
    """

    channel = models.CharField('canal', max_length=64, default='')
    code = models.CharField('cd_canal', max_length=3)

    class Meta:
        verbose_name_plural = 'canais'
        verbose_name = 'canal'


class Skill(BaseModel):
    """
    Classe Channel (Skills)
    Estabelece os skills no modelo base.
    """
    id = models.IntegerField(primary_key=True)
    skil_name = models.CharField('nm_skill', max_length=10)
    assistant_apikey = models.CharField('assistant_apikey', max_length=64,default='')
    assistant_id = models.CharField('assistant_id', max_length=64, default='')
    assistant_url = models.CharField('assistant_url', max_length=256, default='')
    assistant_version = models.CharField('assistant_version', max_length=32, default='')

    class Meta:
        verbose_name_plural = 'skills'
        verbose_name = 'skill'


class ChannelSkill(BaseModel):
    """
    Classe ChannelSkill
    Estabelece a relação entre os canais e as skills watson no modelo base.
    """

    # models.ForeignKey(Channel, on_delete=models.CASCADE)
    # models.ForeignKey(Skill, on_delete=models.CASCADE)

    channel = models.CharField('canal', max_length=10, default='')
    step = models.IntegerField('step', default=0)
    started = models.BooleanField('ativo', default=True)
    id_skil = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'canal_skill'
        verbose_name = 'canal_skill'


class RangeIntents(BaseModel):
    confidance_min = models.DecimalField('grau_confianca_intencao', max_digits=16, decimal_places=2, default=0)
    confidance_max = models.DecimalField('grau_confianca_intencao', max_digits=16, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'intervalo_intencao'
        verbose_name = 'canal_Skill'
# TODO : apagar os create dos modelos OK
# TODO : colocar nomes em PT no admin OK


class TaxPayment(BaseModel):
    """
             Name            : TaxPayment
            :class           : Class TaxPayment
            :create          : julho-2021
            :Models          : auto complete, char and float
            description      :     Gerencia todo tipo de pagamento bancário enviado pelo Watson
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """
    id_tax_payment = models.BigAutoField(primary_key=True)
    tax_type = models.CharField('Tipo da taxa', max_length=32, default='')
    tax_name = models.CharField('Nome da taxa', max_length=32, default='')
    tax_value = models.FloatField("Valor da taxa", default=0.0)


class GuidePost(BaseModel):
    """
             Name            : GuidePost
            :class           : Class TaxPayment
            :create          : setembro-2021
            :Models          : auto complete, char and float
            description      :     Gerencia os postos de atendimento Poupatempo
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    id_guide_post = models.BigAutoField(primary_key=True)
    id_post_guide = models.IntegerField('Id posto guia')
    id_1 = models.CharField(max_length=6, default='',null=True)
    id_8 = models.IntegerField(null=True)
    id_2 = models.IntegerField(null=True)
    id_16 = models.IntegerField(null=True)
    description = models.CharField('Descrição do posto de atendimento', max_length=64, default='', null=True)
    address = models.CharField('Endereço de posto', max_length=256, default='', null=True)
    city = models.CharField('Cidade do posto', max_length=64, default='')


class PostService(BaseModel):
    """
             Name            : GuidePost
            :class           : Class TaxPayment
            :create          : setembro-2021
            :Models          : auto complete, char and float
            description      :     Gerencia os serviços dos postos de atendimento Poupatempo
    ___________________________________________________________________________________________________
    Todos direitos reservados à Magna Sistemas                      (▀̿̿Ĺ̯̿▀̿ ̿)
    """

    id_post_service = models.BigAutoField(primary_key=True)
    id_service = models.IntegerField('Id serviço')
    id_guide_post = models.IntegerField()
    description = models.CharField('Descrição do serviço do posto de atendimento', max_length=256, default='', null=True)
    id_organ = models.IntegerField(null=True)
    validator_ne = models.BooleanField(null=True)
    validator_s = models.BooleanField(null=True)
    validator_sa = models.BooleanField(null=True)




