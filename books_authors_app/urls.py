from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('authors', views.author),
    path('add_author', views.add_author),
    path('book_desc/<int:id>', views.book_desc),
    path('author_desc/<int:id>', views.author_desc)
]