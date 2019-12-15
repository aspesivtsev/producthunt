from django.urls import path

from . import views

urlpatterns = [
    path('', views.test_account, name='accounts_detail'),
    #path('<int:blog_id>/', views.detail, name='detail'),
]