from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=12)
    meli_code=models.CharField(max_length=12)
    image=models.ImageField(upload_to='media/photo')

    def __str__(self):
        return self.user.username