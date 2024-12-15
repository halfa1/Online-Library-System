from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    #path('',views.booklists,name='booklists'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('upload/', views.upload_book, name='upload_book'),
    path('request-book/', views.request_book, name='request_book'),

]
