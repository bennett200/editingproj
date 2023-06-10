from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('letter', views.LetterView.as_view(), name='letter'),
    path('letter/create', views.CreateLetterView.as_view(), name='create_letter'),
    path('letter/<slug:pk>/update', views.UpdateLetterView.as_view(), name='update_letter'),
    path('letter/update/delete', views.DeleteLetterView.as_view(), name='delete_letter'),
]