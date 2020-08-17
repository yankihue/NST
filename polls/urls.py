from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('submit/', views.submit, name='submit'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
    path('<slug:slug>/', views.post_detail, name='detail'),
]
    
