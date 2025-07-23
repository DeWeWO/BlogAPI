from .models import Category, Post
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(trim_whitespace=False, style={'input_type': 'password'})
    password2 = serializers.CharField(trim_whitespace=False, style={'input_type': 'password'})
    
    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")
        if password1 != password2:
            raise serializers.ValidationError(detail={"password2": "Parollar bir xil emas, tekshirib qayta kiriting!"})
        return attrs
    
    def create(self, validated_data):
        password1 = validated_data.pop("password1", "")
        password2 = validated_data.pop("password2", "")
        user = User.objects.create(**validated_data)
        user.set_password(password1)
        user.save()
        token = Token.objects.create(user=user)
        return token
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(trim_whitespace=False, style={'input_type': 'password'})
    
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = User.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError(detail={"email": "Not'g'ri email!"})
        if not user.check_password(password):
            raise serializers.ValidationError(detail={"password": "Not'g'ri parol!"})
        return attrs
    
    def create(self, validated_data):
        email = validated_data.get("email")
        user = User.objects.filter(email=email).first()
        token, created = Token.objects.get_or_create(user=user)
        return token


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
    
    def create(self, validated_data):
        request = self.context.get("request")
        return Post.objects.create(author=request.user, **validated_data)
    
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "description", "image", "views", "author", "category"]
        read_only_fields = ["id", "slug", "views", "author"]

