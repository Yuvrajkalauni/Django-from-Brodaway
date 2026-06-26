from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    discription = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(
        max_length = 10,
        choices = {
            'L' : 'Low',
            'M' : 'Medium',
            'H' : 'High'
        },
        default = 'Low'
    )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'Task'

    def __str__ (self):
        return self.title
