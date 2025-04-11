from django.db import models
from django.conf import settings

Quiz = settings.QUIZ_MODEL

class QuizAnalytics(models.Model):
    quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    average_score = models.FloatField()
    best_score = models.PositiveIntegerField()
