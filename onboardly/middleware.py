from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import redirect_to_login

class LoginRequiredMiddleware:
    """Обработка не зарегестрированных пользователей"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith(reverse('admin:index')) or request.path.startswith(reverse('login')) or request.path.startswith(reverse('register')):
            return None

        if not request.user.is_authenticated:
            if request.path != reverse('register'):
                return redirect(reverse('register'))

        return None