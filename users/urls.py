from django.urls import path
from django.contrib.auth.views import LoginView

from users.views import RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]