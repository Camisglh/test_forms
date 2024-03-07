from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Poll(models.Model):
    """Опросы на странице"""

    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=255)


class Question(models.Model):
    """
    Модель для вопросов
    Используйте depends_on как идет после X(вопроса)
    Используйте depends_on_answer как появляется при X(ответе)
    """

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    depends_on = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dependents",
    )
    depends_on_answer = models.ManyToManyField(
        "Answer", blank=True, related_name="dependent_questions"
    )

    def __str__(self):
        return self.text


class Answer(models.Model):
    """Модель для варианта ответов на вопросы"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    type = models.CharField(
        max_length=100, choices=[("text", "Text"), ("option", "Options")]
    )

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    """Модель для сохранения ответов пользователей"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
