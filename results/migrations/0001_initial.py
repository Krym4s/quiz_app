# Generated by Django 5.2 on 2025-04-04 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField()),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz')),
            ],
        ),
    ]
