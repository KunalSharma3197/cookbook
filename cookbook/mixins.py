from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AuthorTimeStampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_by = models.ForeignKey(
    User, 
    on_delete=models.CASCADE, 
    related_name="%(class)s_created_by"
  )
  updated_by = models.ForeignKey(
    User, 
    on_delete=models.CASCADE, 
    related_name="%(class)s_updated_by"
  )

  class Meta:
    abstract = True


class IsDeletedMixin(models.Model):
  is_deleted = models.BooleanField(default=False)

  class Meta:
    abstract = True


class BaseApiMixin(APIView):
  post_serializer_class = None
  patch_serializer_class = None
  serializer_class = None

  def get_object_or_404(self, pk):
    try:
      return self.get_queryset().get(pk=pk)
    except self.get_queryset().model.DoesNotExist:
      return Response(
        {"error": "Object not found"}, 
        status=status.HTTP_404_NOT_FOUND
      )

  def perform_create(self, request):
    if self.post_serializer_class:
      serializer = self.post_serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save(created_by=request.user, updated_by=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(
      {"error": "Post serializer not configured"}, 
      status=status.HTTP_400_BAD_REQUEST
    )

  def perform_update(self, request, pk):
    if not self.patch_serializer_class:
      return Response(
        {"error": "Patch serializer not configured"}, 
        status=status.HTTP_400_BAD_REQUEST
      )

    instance = self.get_object_or_404(pk)
    if isinstance(instance, Response):
      return instance

    print("request.data, instance", request.data, instance)
    serializer = self.patch_serializer_class(
      instance, 
      data=request.data, 
      partial=True
    )
    serializer.is_valid(raise_exception=True)
    serializer.save(updated_by=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
