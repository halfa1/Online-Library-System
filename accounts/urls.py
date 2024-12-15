from django.urls import path
from bookstore.views import booklists
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', booklists, name='bookslist'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
