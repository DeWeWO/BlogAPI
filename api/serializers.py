from .models import Category, Post
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200, required=True)
    slug = serializers.SlugField(read_only=True)
    description = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategorySerializer(instance=instance.category).data
        data["author"] = instance.author.username
        return data
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "description", "image", "views", "author", "category"]
        read_only_fields = ["id", "slug"]