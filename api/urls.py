from django.urls import path
from .views import SignUpView, LogInView, getAuthenticatedUser, ListAllBooksView, LogOutView, AddBookView

urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('log-in', LogInView.as_view()),
	path('log-out', LogOutView.as_view()),
    path('get-user/<str:token>', getAuthenticatedUser.as_view()),
    path('list-books', ListAllBooksView.as_view()),
	path('add-book', AddBookView.as_view()),
]
