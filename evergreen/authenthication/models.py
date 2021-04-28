from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtraInfo(models.Model):
    id = models.AutoField(primary_key= True)
    userType = models.CharField(max_length= 120)
    regist_date = models.DateTimeField(auto_now= True)
    userId = models.ForeignKey(User, on_delete= models.CASCADE, null= True)