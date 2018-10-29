from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^registrar/$',correo_celery, name = "register"),
	url(r'^basic_view/$', basic_view, name = "basic_view"),
	url(r'^table_esui/$', table_esui, name = "table_esui"),
	url(r'^vistas_tabla/$', vistas_tabla, name = "vistas_tabla"),
	url(r'^test_api/$', EntidadViewSet2.as_view(), name = "test_api"),
	url(r'^api_prueba/$', PruebaViewSet.as_view(), name = "api_prueba"),
	url(r'^test_form/$', test_form, name = "test_form"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)