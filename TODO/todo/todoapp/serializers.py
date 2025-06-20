from rest_framework import serializers
from .models import TodoItem  

class TodoItemSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = TodoItem
        fields = ['title', 'description', 'is_completed', 'created_at']
