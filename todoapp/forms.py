
from django import forms
from .models import TodoItem
 
 
# creating a form
class TodoItemForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = TodoItem
 
        # specify fields to be used
        fields = [
            "note"
        ]