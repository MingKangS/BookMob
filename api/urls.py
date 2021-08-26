from django.urls import path
from .views import SignUpView, LogInView, getAuthenticatedUser

urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('log-in', LogInView.as_view()),
    path('get-user/<str:token>', getAuthenticatedUser.as_view()),
]
