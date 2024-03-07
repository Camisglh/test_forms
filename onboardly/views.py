from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Poll, Question, Answer, UserResponse
from .question_services import (
    get_poll_list,
    get_question_or_404,
    save_user_response,
    get_next_question_id,
)


def register(request):
    """Регистрация пользователя"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


@login_required
def poll_list(request):
    """Отображение списка опросов"""
    polls = get_poll_list()
    return render(request, "poll_list.html", {"polls": polls})


@login_required
def show_question(request, poll_id, question_id=None):
    """Отображение вопроса и обработка ответа пользователя"""
    poll = get_object_or_404(Poll, id=poll_id)
    question = get_question_or_404(poll, question_id)
    answer_set = question.answer_set.all()
    answer_type = question.answer_set.first().type if answer_set.exists() else "text"

    if request.method == "POST":
        user = request.user
        answer_id = request.POST.get("answer_id")
        answer_text = request.POST.get("text_answer")

        save_user_response(user, poll, question, answer_type, answer_id, answer_text)

        next_question_id = get_next_question_id(question, answer_type, answer_id)

        if next_question_id:
            return redirect(
                "show_question", poll_id=poll_id, question_id=next_question_id
            )
        else:
            return redirect("/")

    return render(
        request,
        "question.html",
        {"question": question, "answer_set": answer_set, "answer_type": answer_type},
    )
