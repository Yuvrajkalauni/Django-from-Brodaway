from django.db import models

# Create your models here.


#-------------------- Subscription Plan --------------------

class SubscriptionPlan (models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10)
    duration_day = models.PositiveIntegerField(help_text="Duration in days")
    is_active = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class meta:
        db_table = "Subscription Plan"