from django.db import models
from django.core.validators import MinValueValidator
from cookbook.mixins import AuthorTimeStampedModel, IsDeletedMixin
from profiles.models import Author
from utils.models import File

# Create your models here.
class Recipe(AuthorTimeStampedModel, IsDeletedMixin):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Preparation time in minutes"
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="recipes")
    servings = models.IntegerField(
        validators=[MinValueValidator(1)],
        default=1
    )
    image = models.ForeignKey(File, on_delete=models.CASCADE, related_name="recipes")
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='medium'
    )

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['difficulty']),
        ]

    def __str__(self):
        return self.name

    def clean(self):
        if self.prep_time < 1:
            raise models.ValidationError("Preparation time must be at least 1 minute")
        if self.servings < 1:
            raise models.ValidationError("Servings must be at least 1")
