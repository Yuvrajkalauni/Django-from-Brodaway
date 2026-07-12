from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#-------------------- Subscription Plan --------------------

class SubscriptionPlan (models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_day = models.PositiveIntegerField(help_text="Duration in days")
    is_active = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class meta:
        db_table = "Subscription Plan"

    

#-------------------- Subscription Plan --------------------

class UserSubscriptionStatus(models.TextChoices):
        ACTIVATE = 'Activate'
        EXPIRED = 'Expired'
        CANCELLED = 'Cancelled'
        PENDING = 'Pending'
        PAUSED = 'Paused'
        FAILED = 'Failed'

class UserSubscription (models.Model):
     user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "Subscriptions")
     plan = models.ForeignKey(SubscriptionPlan, on_delete = models.CASCADE, related_name = "User Subscriptions")
     start_data = models.Datafield()
     end_date = models.DateField()
     status = models.CharField(max_length = 20, choices = UserSubscriptionStatus.choices, default = UserSubscriptionStatus.PENDING)

     def _str_(self):
          return f"{self.user.username}-{self.plan}({self.status})"
     
     class meta:
          db_table = "User Subscription"
