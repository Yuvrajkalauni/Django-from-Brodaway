from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.IntegerField(null=True)

    class Meta:
        db_table = "Things"

    def __str__(self):
        return f'{self.name}'