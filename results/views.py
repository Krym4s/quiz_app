from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from results.models import QuizResult, StudentAnswer

@login_required
def results_list(request):
    """Список результатов пользователя"""
    results = QuizResult.objects.filter(student=request.user)
    return render(request, 'results/results_list.html', {'results': results})

@login_required
def result_detail(request, result_id):
    """Детализация результата"""
    result = get_object_or_404(QuizResult, id=result_id, student=request.user)
    answers = StudentAnswer.objects.filter(student=request.user, question__quiz=result.quiz)
    return render(request, 'results/result_detail.html', {'result': result, 'answers': answers})
