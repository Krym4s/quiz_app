from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
Quiz = settings.QUIZ_MODEL
Question = settings.QUESTION_MODEL
Answer = settings.ANSWER_MODEL

class QuizResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    score = models.PositiveIntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)
    time_spent = models.PositiveIntegerField(default=0)

class StudentAnswer(models.Model):
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)  # Для текстовых ответов
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)  # Для выбора варианта
    is_correct = models.BooleanField(default=False)