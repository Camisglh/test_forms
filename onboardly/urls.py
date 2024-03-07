from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

"""
Первый путь идет к списку всех опросов, далее мы получаем опрос по его id и
текущий вопрос который идет сейчас. Далее два пути регистрации и логина 
"""

urlpatterns = [
    path("", views.poll_list, name="poll_list"),
    path(
        "poll/<int:poll_id>/question/<int:question_id>/",
        views.show_question,
        name="show_question",
    ),
    path("register/", views.register, name="register"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
]
