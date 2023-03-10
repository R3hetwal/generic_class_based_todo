from users.models import NewUser
from django.db import models
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


    class Meta:
        order_with_respect_to = 'user'