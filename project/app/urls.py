from django.urls import path,include
from app import views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('news/',views.news,name='news')

]