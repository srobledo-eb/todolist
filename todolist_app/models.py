from django.db import models
from django.conf import settings


class Priority(models.Model):
    description = models.CharField(max_length=30)
    order = models.IntegerField()
    def __str__(self):
        return self.description

class Todo(models.Model):
    description = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    def __str__(self):
        return self.description
