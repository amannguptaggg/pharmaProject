from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index/',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('courses/',views.courses,name='courses'),
    path('logout/',views.logout,name='logout'),
    
]
