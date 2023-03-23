from django.db import models

# Create your models here.
class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(null=False)
    current_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.description
    
