from django_filters import FilterSet, CharFilter, NumberFilter, ChoiceFilter
from .models import Recipe

class RecipeFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    ingredients = CharFilter(lookup_expr='icontains')
    instructions = CharFilter(lookup_expr='icontains')
    prep_time_min = NumberFilter(field_name='prep_time', lookup_expr='gte')
    prep_time_max = NumberFilter(field_name='prep_time', lookup_expr='lte')
    servings_min = NumberFilter(field_name='servings', lookup_expr='gte')
    servings_max = NumberFilter(field_name='servings', lookup_expr='lte')
    difficulty = ChoiceFilter(choices=Recipe.DIFFICULTY_CHOICES)

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'instructions', 'prep_time', 'servings', 'difficulty']