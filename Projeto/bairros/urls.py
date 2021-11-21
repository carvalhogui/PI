from . import views
from django.conf.urls import url 
from django.urls import path

urlpatterns = [
	# /pagina_inicial/
    url('pagina_inicial', views.index, name='index'),

    # /sobre_nos/
    url('sobre_nos', views.sobre_nos, name='sobre_nos'),

    # /pesquisar_por_bairro/
    url('pesquisar_por_bairro', views.pesquisar_por_bairro, name='pesquisar_por_bairro'),

    # /pesquisar_por_logradouro/
    url('pesquisar_por_logradouro', views.pesquisar_por_logradouro, name='pesquisar_por_logradouro')
]
