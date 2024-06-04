from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('contact',views.contact,name='contact'),
    path('login',views.home,name='login'),
    path('about', views.home, name='about'),
    path('package', views.home, name='package'),

    ]

