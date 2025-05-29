from django.urls import path
from .views import RecipeView

urlpatterns = [
    path('recipies/', RecipeView.as_view(), name='recipie-list'),
    path('recipies/<int:pk>/', RecipeView.as_view(), name='recipie-detail'),
]