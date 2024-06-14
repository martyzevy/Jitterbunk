from django.urls import path

from . import views

app_name = 'jitter'
urlpatterns = [
    path('', views.BunkView.as_view(), name='bunks'),
    path('<int:pk>/', views.IndividualsView.as_view(), name='individuals'),
    path('newbunkform/', views.get_bunking_users, name='bunk')
]