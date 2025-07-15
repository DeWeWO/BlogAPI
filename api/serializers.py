from datetime import datetime
from rest_framework import serializers

class Comment:
    def __init__(self, email, content, created = None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

# comment1 = Comment("admin@gmail.com", "test comment content")

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(min_length=3, max_length=1024)
    created = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Comment(**validated_data)