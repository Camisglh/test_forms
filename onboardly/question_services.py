from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Poll, Question, Answer, UserResponse


def get_poll_list():
    """Получение списка опросов"""
    polls = Poll.objects.all()
    for poll in polls:
        first_question = Question.objects.filter(
            poll=poll, depends_on__isnull=True, depends_on_answer__isnull=True
        ).first()
        poll.first_question_id = first_question.id if first_question else None
    return polls


def get_question_or_404(poll, question_id):
    """Получение вопроса или возврат ошибки"""
    if question_id is None:
        return Question.objects.filter(poll=poll, depends_on__isnull=True).first()
    else:
        return Question.objects.get(id=question_id, poll=poll)


def save_user_response(user, poll, question, answer_type, answer_id, answer_text):
    """Сохранение ответа пользователя"""
    if answer_type == "text" and answer_text:
        answer = Answer.objects.create(question=question, text=answer_text, type="text")
    elif answer_type == "option" and answer_id:
        answer = Answer.objects.get(id=answer_id)
    else:
        return

    UserResponse.objects.create(user=user, poll=poll, question=question, answer=answer)


def get_next_question_id(question, answer_type, answer_id):
    """Определение следующего вопроса на основе ответа пользователя"""
    if answer_type == "text":
        next_question = Question.objects.filter(depends_on=question).first()
    elif answer_type == "option":
        next_questions = Question.objects.filter(
            depends_on=question, depends_on_answer__id=answer_id
        )
        next_question = next_questions.first() if next_questions.exists() else None
    else:
        next_question = None

    return next_question.id if next_question else None
