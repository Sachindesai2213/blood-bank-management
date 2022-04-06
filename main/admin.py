from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BloodType)
admin.site.register(UserPersonalInfo)
admin.site.register(Requirement)
admin.site.register(RequirementDonors)