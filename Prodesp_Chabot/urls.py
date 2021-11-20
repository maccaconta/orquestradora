from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.conf import settings

# drf_yasg('swagger') code starts here
from rest_framework import permissions
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.static import  static

router = routers.SimpleRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Orchest API",
        default_version='v1',
        description="API fornece serviços de ...",
        terms_of_service="URL_AQUI",
        # contact=openapi.Contact(email="email@email.org"),
        # license=openapi.License(name="DESCRIPTION"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ends here


urlpatterns = [
    path('admin/', admin.site.urls),
    path('orchest/v1/', include('api.urls')),
    path('orchest/v1/middle/', include('middle.urls')),
    path('orchest/v1/broadcast/', include('broadcast.urls')),
    path('auth/', include('rest_framework.urls')),
    path('orchest/v1/info/', schema_view.with_ui(
        'swagger', cache_timeout=0),
         name='schema-swagger-ui')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

