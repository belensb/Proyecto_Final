from django.urls import path
from. import views


urlpatterns = [
    path ('ver-publicaciones/',views.publicaciones_view, name='publicaciones' )
]