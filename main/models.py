from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BloodType(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=10)


class UserPersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    age = models.IntegerField()
    contact = models.CharField(max_length=50)
    is_active_donor = models.BooleanField(default=False)


class Requirement(models.Model):
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requirement_fulfilled = models.BooleanField(default=False)


class RequirementDonors(models.Model):
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    acceptance_status = models.BooleanField(default=False)
