from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('services', views.services),
    path('contact', views.contact),
    path('blog', views.blog),
    path('gallery', views.gallery),
    path('portfolio', views.portfolio),
    path('pricing', views.pricing),

]