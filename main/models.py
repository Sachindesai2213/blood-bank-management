from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BloodType(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class UserPersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bloodType = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.TimeField()
    contact = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username
