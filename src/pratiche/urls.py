from django.contrib import admin
from django.urls import path, include
from . import views

app_name='pratiche'
urlpatterns = [
    path('', views.pratica_list_view, name='pratica-list'), 
    # path('crea/', pratica_create_view, name='pratica-create'),
    path('add/', views.PraticaCreateView.as_view(), name='pratica-add'),
    path('add/agente', views.AgenteCreateView.as_view(), name='agente-add'),
    path('add/magistrato', views.MagistratoCreateView.as_view(), name='magistrato-add'),
    path('add/indagato', views.IndagatoCreateView.as_view(), name='indagato-add'),
    path('list/indagato',views.indagato_list_view, name = 'indagato-list'),
    path('list/agente', views.AgenteListView.as_view(), name='agente-list'),
    path('list/magistrato', views.MagistratoListView.as_view(), name='magistrato-list'),
    path('indagato/<int:pk>/',views.pratiche_indagato.as_view(), name='pratiche-indagato'),
    path('agente/<int:id>/',views.pratiche_agente.as_view(), name='pratiche-agente'),
    path('magistrato/<int:id>/',views.pratiche_magistrato.as_view(), name='pratiche-magistrato'),
    #path('indagato/<int:pk>/',views.pratiche_indagato, name='pratiche-indagato'),
    #path('<int:id>/', views.pratica_detail_view, name='pratica-detail'),
    path('<int:id>/', views.PraticaDetailView.as_view(), name='pratica-detail'),
    # path('<int:id>/modifica/', pratica_update_view, name='pratica-update'),    
    # path('<int:id>/elimina/', pratica_delete_view, name='pratica-delete'),
    path('signup/',views.SignUp.as_view(), name='signup'),
    path('ajax/load-prot/', views.load_prot, name='load_prot'),
    ]