from rest_framework import serializers
from .models import Recipe
from profiles.models import Author
from profiles.serializers import AuthorSerializer
from utils.serializers import FileSerializer

class RecipeSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    image = FileSerializer(read_only=True)
    prep_time_display = serializers.SerializerMethodField()
    difficulty_display = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            'id', 'name', 'description', 'ingredients', 'instructions',
            'prep_time', 'prep_time_display', 'difficulty', 'difficulty_display',
            'servings', 'author', 'image', 'created_at', 'updated_at', 'created_by', 'updated_by'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by', 'updated_by', 'author', 'image']

    def get_prep_time_display(self, obj):
        hours = obj.prep_time // 60
        minutes = obj.prep_time % 60
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"

    def get_difficulty_display(self, obj):
        return obj.get_difficulty_display()

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Recipe name must be at least 3 characters long")
        return value

    def validate_ingredients(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Ingredients list must be more detailed")
        return value

    def validate_instructions(self, value):
        if len(value.strip()) < 20:
            raise serializers.ValidationError("Instructions must be more detailed")
        return value

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user.author
        print(validated_data)
        return super().create(validated_data)

class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'name', 'description', 'ingredients', 'instructions',
            'prep_time', 'author', 'servings', 'image', 'difficulty'
        ]

    def validate(self, data):
        if data.get('prep_time', 0) < 1:
            raise serializers.ValidationError("Prep time must be at least 1 minute")
        if data.get('servings', 0) < 1:
            raise serializers.ValidationError("Servings must be at least 1")
        return data

    def create(self, validated_data):
        author = validated_data['author']
        created_by = author.user
        validated_data['created_by'] = created_by
        validated_data['updated_by'] = created_by
        return super().create(validated_data)

class RecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'name', 'description', 'ingredients', 'instructions',
            'prep_time', 'author', 'servings', 'image', 'difficulty'
        ]
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'ingredients': {'required': False},
            'instructions': {'required': False},
            'prep_time': {'required': False},
            'author': {'required': False},
            'servings': {'required': False},
            'image': {'required': False},
            'difficulty': {'required': False}
        }

    def validate(self, data):
        if 'prep_time' in data and data['prep_time'] < 1:
            raise serializers.ValidationError("Prep time must be at least 1 minute")
        if 'servings' in data and data['servings'] < 1:
            raise serializers.ValidationError("Servings must be at least 1")
        return data

    def update(self, instance, validated_data):
        validated_data['updated_by'] = instance.created_by
        return super().update(instance, validated_data)


