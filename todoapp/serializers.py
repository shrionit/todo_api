from .models import *
from rest_framework.serializers import ModelSerializer

class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'