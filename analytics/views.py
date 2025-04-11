from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from results.models import QuizResult
from django.db.models import Avg
import json

@login_required
def analytics_dashboard(request):
    """Дашборд с аналитикой"""
    # Данные для графика пользователя
    user_results = QuizResult.objects.filter(student=request.user)
    quiz_titles = [result.quiz.title for result in user_results]
    user_scores = [result.score for result in user_results]
    
    # Средние результаты по всем тестам
    avg_scores = []
    for quiz_title in quiz_titles:
        avg = QuizResult.objects.filter(quiz__title=quiz_title).aggregate(Avg('score'))['score__avg']
        avg_scores.append(avg or 0)
    
    context = {
        'quiz_titles': json.dumps(quiz_titles),
        'user_scores': json.dumps(user_scores),
        'avg_scores': json.dumps(avg_scores),
    }
    
    return render(request, 'analytics/dashboard.html', context)
