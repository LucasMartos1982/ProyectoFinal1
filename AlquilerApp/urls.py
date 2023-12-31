from django.urls import path
from AlquilerApp import views
from django.contrib.auth.views import LogoutView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('estudio/',views.estudio,name='Estudio'),
    path('alquiler/',views.alquiler,name='Alquiler'),
    path('clientes/',views.clientes,name='Clientes'),
       
    path('cliente/list',views.ClienteList.as_view(),name='List'),
    path('cliente/<pk>',views.ClienteDetalle.as_view(),name='Detail'),
    path('cliente/nuevo/',views.ClienteCreacion.as_view(),name='New'),
    path('cliente/editar/<pk>',views.ClienteUpdate.as_view(),name='Edit'),
    path('cliente/delete/<pk>',views.ClienteDelete.as_view(),name='Delete'),
    
    path('articulo/list',views.ArticulosList.as_view(),name='Art_List'),
    path('articulo/<pk>',views.ArticulosDetalle.as_view(),name='Art_Detail'),
    path('articulo/nuevo/',views.ArticulosCreacion.as_view(),name='Art_New'),
    path('articulo/editar/<pk>',views.ArticulosUpdate.as_view(),name='Art_Edit'),
    path('articulo/delete/<pk>',views.ArticulosDelete.as_view(),name='Art_Delete'),
    
    path('estudio/logout',LogoutView.as_view(template_name='EstenopoApp/home.html'), name='Logout'),
    

    
]
#urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)