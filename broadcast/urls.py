
from broadcast.views import ApiWebHooksWhatsapp, ApiLogado, removeWhats
from django.urls import path, re_path

urlpatterns = [
    path('whats/', ApiWebHooksWhatsapp.as_view()),
    path('removeWhats/', removeWhats, name='removeWhats'),
    path('logado/', ApiLogado.as_view())
]

