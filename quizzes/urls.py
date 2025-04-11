from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('<int:quiz_id>/start/', views.quiz_start, name='quiz_start'),
    path('<int:quiz_id>/submit/', views.quiz_submit, name='quiz_submit'),
    path('create/', views.create_quiz, name='create_quiz'),
    path('<int:quiz_id>/add-questions/', views.add_questions, name='add_questions'),
    path('question/<int:question_id>/add-answers/', views.add_answers, name='add_answers'),
]