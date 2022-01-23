from django.db import models
from django.urls import reverse

class TodoItem(models.Model):
    note = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.note

    def get_absolute_url(self):
        return reverse("TodoItem_detail", kwargs={"pk": self.pk})