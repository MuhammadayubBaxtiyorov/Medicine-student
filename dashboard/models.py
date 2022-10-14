from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()



class Illness(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    identified_time = models.DateField()
    identified_by = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Medicine(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    illness  = models.ForeignKey(Illness, on_delete=models.CASCADE)
    
    
    
class Times(models.Model):
    alert = models.TimeField()
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    

class NotificationPerson(models.Model):
    who =  models.CharField(max_length=255)
    telegram_id = models.CharField(max_length=400)
    first_name = models.CharField(max_length=255)
    who_2 =  models.CharField(max_length=255)
    telegram_id_2 = models.CharField(max_length=400)
    first_name_2 = models.CharField(max_length=255)
    user  = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
