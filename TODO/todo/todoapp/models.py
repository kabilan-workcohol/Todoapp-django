from django.db import models

class TodoItem(models.Model):  
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title
