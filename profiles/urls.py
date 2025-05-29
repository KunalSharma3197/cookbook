from django.urls import path
from .views import AuthorView

urlpatterns = [
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorView.as_view(), name='author'),
]
