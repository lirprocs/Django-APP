from django.shortcuts import render, redirect
import random
from .utils import check_access_code, generate_access_code
from .models import Question, AccessCode, TestResult
from django.contrib.auth.decorators import login_required


@login_required
def process_code(request):
    if request.method == 'POST':
        class_level = int(request.POST['class_level'])  # Получите класс от пользователя
        access_code = generate_access_code(class_level)

        # Сохраните код доступа и класс в базе данных
        access_code_instance = AccessCode.objects.create(code=access_code, class_level=class_level)

        # Перенаправление на страницу с кодом доступа
        return redirect('code_display', access_code=access_code)

    return render(request, 'examination/template.html')


def select_random_questions(class_level, num_questions):
    questions = Question.objects.filter(clas=class_level)
    if len(questions) < num_questions:
        raise Exception("Недостаточно вопросов для теста.")

    random_questions = random.sample(list(questions), num_questions)
    return random_questions


def take_test(request, access_code):
    if request.method == 'POST':
        access_code = request.POST.get('access_code')
    class_level = int(access_code.split('_')[0])
    num_questions = 15
    questions = select_random_questions(class_level, num_questions)

    if request.method == 'POST':
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}', '')
            is_correct = user_answer == question.answer
            TestResult.objects.create(user=request.user, question=question, user_answer=user_answer,
                                      is_correct=is_correct)
        return redirect('test_results')

    return render(request, 'examination/test_template.html', {'questions': questions})


@login_required
def enter_code(request):
    if request.method == 'POST':
        access_code = request.POST['access_code']

        if check_access_code(access_code):
            return redirect('take_test', access_code=access_code)
        else:
            error_message = "Invalid access code."
            return render(request, 'examination/enter_code.html', {'error_message': error_message})

    return render(request, 'examination/enter_code.html')


def submit_test(request):
    if request.method == 'POST':
        access_code = request.POST['access_code']
        class_level = int(access_code.split('_')[0])
        questions = select_random_questions(class_level, num_questions=15)

        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}', '')
            is_correct = user_answer == question.answer
            TestResult.objects.create(user=request.user, question=question, user_answer=user_answer,
                                      is_correct=is_correct)

        return redirect('examination/test_results')


def test_results(request):
    test_results = TestResult.objects.filter(user=request.user)
    return render(request, 'test_results.html', {'test_results': test_results})


def code_display(request, access_code):
    return render(request, 'examination/display_code_template.html', {'access_code': access_code})

