from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#-------------------- Subscription Plan --------------------

class SubscriptionPlan (models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(
         max_digits=10,
         decimal_places=2
         )
    duration_day = models.PositiveIntegerField(help_text="Duration in days")
    is_active = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class meta:
        db_table = "Subscription Plan"

    

#-------------------- User Subscription --------------------

class UserSubscriptionStatus(models.TextChoices):
        ACTIVATE = 'Activate'
        EXPIRED = 'Expired'
        CANCELLED = 'Cancelled'
        PENDING = 'Pending'
        PAUSED = 'Paused'
        FAILED = 'Failed'

class UserSubscription (models.Model):
     user = models.ForeignKey(
          User,
          on_delete = models.CASCADE,
          related_name = "Subscriptions"
          )
     plan = models.ForeignKey(
          SubscriptionPlan, 
          on_delete = models.CASCADE, 
          related_name = "UserSubscriptions"
          )
     start_data = models.DateField()
     end_date = models.DateField()
     status = models.CharField(
          max_length = 20, 
          choices = UserSubscriptionStatus.choices, 
          default = UserSubscriptionStatus.PENDING
          )

     def _str_(self):
          return f"{self.user.username}-{self.plan}({self.status})"
     
     class meta:
          db_table = "User_Subscription"



#-------------------- Payment --------------------

class PaymentMethod (models.TextChoices):
     ESEWA = "esewa"
     KHALTI = "khalti"
     BANK_TRANSFER = "bank_transfer"
     CASH = "cash"

class PaymentStatus (models.TextChoices):
     PENDING = "pending"
     SUCESS = "success"
     FAILED = "failed"

class Payment (models.Model):
     Subscription = models.ForeignKey(
          UserSubscription, 
          on_delete = models.CASCADE, 
          related_name = "payments"
          )
     amount = models.DecimalField(
          max_digits=8,
          decimal_places=2
          )
     payment_method = models.CharField(
          max_length = 20, 
          choices = PaymentMethod.choices, 
          default = PaymentMethod.KHALTI
          )
     transaction_id = models.CharField(
          max_length=100,
          null = True,
          blank = True
          )
     status = models.CharField(
          max_length=20,
          choices=PaymentStatus.choices,
          default=PaymentStatus.PENDING
     )
     pidx=models.CharField(
          max_length=50,
          null=True,
          blank=True
     )

     def __str__(self):
          return f"{self.transaction_id}-{self.status}"
     
     class meta:
          db_table = "payments"

