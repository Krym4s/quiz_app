from django.urls import path
from . import views

urlpatterns = [
    path('', views.results_list, name='results_list'),
    path('<int:result_id>/', views.result_detail, name='result_detail'),
]