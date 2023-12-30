from django.urls import path
from . import views

urlpatterns = [
    path('set_cookies', views.set_cookies, name='set_cookie'),
    path('', views.set_session, name='set_session'),
    path('delete_session/', views.delete_session, name='delete_session'),
    path('session/', views.get_session, name='get_session'),
    path('get/', views.get_cookies, name='get_cookies'),
    path('del/', views.delete_cookie, name='delete_cookies'),
]