from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.views import RegisterView

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("", LoginView.as_view(template_name="users/login.html")),
    path("register/", RegisterView.as_view(), name="register"),
]
