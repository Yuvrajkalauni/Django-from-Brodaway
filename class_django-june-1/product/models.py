from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=80, null=True )
    phone = models.IntegerField()
  
    class Meta:
        db_table = 'Ram'
