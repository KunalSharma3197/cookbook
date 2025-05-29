from rest_framework import generics, status
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer, RecipeCreateSerializer, RecipeUpdateSerializer
from cookbook.mixins import BaseApiMixin
from rest_framework import filters

class RecipeView(BaseApiMixin, generics.GenericAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    post_serializer_class = RecipeCreateSerializer
    patch_serializer_class = RecipeUpdateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    def get(self, request, pk=None):
        if pk:
            instance = self.get_object_or_404(pk)
            if isinstance(instance, Response):
                return instance
            serializer = self.serializer_class(instance)
            return Response(serializer.data)

        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return self.perform_create(request)

    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {"detail": "Recipe ID is required for update."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.perform_update(request, pk)
