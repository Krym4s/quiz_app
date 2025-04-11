from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Quiz, Question, Answer
from .forms import QuizCreateForm, QuizForm, QuestionForm, AnswerForm
from django.contrib import messages
from results.models import StudentAnswer, QuizResult

@login_required
def quiz_list(request):
    """Список всех тестов"""
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    """Детали теста"""
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz})

@login_required
def quiz_submit(request, quiz_id, time_spent):
    """Обработка ответов на тест"""
    quiz = get_object_or_404(Quiz, id=quiz_id)
            
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        score = 0

        result = QuizResult.objects.create(
            student=request.user,
            quiz=quiz,
            score=score,
            time_spent = time_spent,
            completed_at=timezone.now()
        )
        
        for question in quiz.question_set.all():
            answer_key = f'question_{question.id}'
            user_answer = request.POST.get(answer_key)
            is_correct = False
            
            if question.question_type == 'MC':
                selected_answer = Answer.objects.get(id=user_answer)
                
                if selected_answer.is_correct:
                    is_correct=True
                    score += 1
                
                StudentAnswer.objects.create(
                    student=request.user,
                    question=question,
                    selected_answer=selected_answer,
                    quiz_result=result,
                    is_correct=is_correct
                )
            else:
                for answer in question.answer_set.all():
                    if answer.text == user_answer and answer.is_correct:
                        is_correct=True
                        score += 1
                        break

                StudentAnswer.objects.create(
                    student=request.user,
                    question=question,
                    answer_text=user_answer,
                    quiz_result=result,
                    is_correct=is_correct
                )

        result.score = score
        result.save()
        
        messages.success(request, f'Тест завершён! Ваш результат: {score}/{quiz.question_set.count()}')
        return redirect('results_list')
    
    return redirect('quiz_list')

@login_required
def quiz_start(request, quiz_id):
    """Страница прохождения теста"""
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    if request.method == 'POST':
        messages.success(request, 'Тест отправлен на проверку!')
        print(request.POST.get('time_spent'))
        return quiz_submit(request, quiz_id, request.POST.get('time_spent'))
    
    if 'quiz_start_time' not in request.session:
        request.session['quiz_start_time'] = timezone.now().timestamp()
        request.session.modified = True
    
    return render(request, 'quizzes/quiz_start.html', {'quiz': quiz})

@login_required
def create_quiz(request):
    if request.method == 'POST':
        quiz_form = QuizCreateForm(request.POST)
        if quiz_form.is_valid():
            quiz = quiz_form.save(commit=False)
            quiz.creator = request.user
            quiz.save()
            return redirect('add_questions', quiz_id=quiz.id)
    else:
        quiz_form = QuizCreateForm()
    
    return render(request, 'quizzes/create_quiz.html', {'form': quiz_form})

@login_required
def add_questions(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question = question_form.save()
            return redirect('add_answers', question_id=question.id)
    else:
        question_form = QuestionForm()
    
    return render(request, 'quizzes/add_questions.html', {
        'quiz': quiz,
        'form': question_form
    })

@login_required
def add_answers(request, question_id):
    question = Question.objects.get(id=question_id)
    
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.question = question 
            answer.save()
            if 'add_more' in request.POST:
                return redirect('add_answers', question_id=question.id)
            return redirect('add_questions', quiz_id=question.quiz.id)
    else:
        answer_form = AnswerForm()
    
    return render(request, 'quizzes/add_answers.html', {
        'question': question,
        'form': answer_form
    })

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'questions/question_form.html', {'form': form})

def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            # Обработка удаления изображения
            if 'image-clear' in request.POST:
                question.image.delete(save=False)
            form.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'questions/question_form.html', {'form': form, 'object': question})
