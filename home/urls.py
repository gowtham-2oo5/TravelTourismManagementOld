from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('services',views.services,name='services'),
]