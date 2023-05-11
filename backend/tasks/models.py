from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.TextField()
    is_important = models.BooleanField()
    is_completed = models.BooleanField()
    deadline = models.DateTimeField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "tasks"

    def __str__(self):
        return self.tittle
