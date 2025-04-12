from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    time_limit = models.PositiveIntegerField(
        default=10,  # 10 минут по умолчанию
        help_text="Лимит времени в минутах"
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_quizzes',
        blank=False,
        #default='1'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField(default='')
    image = models.ImageField(
        upload_to='questions/images/',
        blank=True,
        null=True,
        verbose_name="Изображение"
    )
    question_type = models.CharField(choices=[("MC", "Multiple Choice"), ("TXT", "Text Answer")], max_length=3)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

