from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('letter', views.LetterView.as_view(), name='letter'),
    path('letter/create', views.CreateLetterView.as_view(), name='create_letter')
]