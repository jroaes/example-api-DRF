from django.conf.urls import url
from postulacion import views


urlpatterns = [
    url(r'^persona/$', views.persona_list),
    url(r'^persona/(?P<pk>[0-9]+)/$', views.persona_detail),
]
