from django.db import models
from django.contrib.auth.models import User
import jdatetime


# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {}".format(jdatetime.date(self.date()).strftime("%d - %m - %Y"),self.amount)
    
class Income(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)