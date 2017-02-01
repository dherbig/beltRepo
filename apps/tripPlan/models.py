from __future__ import unicode_literals
from ..loginReg.models import User
from django.db import models

# Create your models here.
class travelPlan(models.Model):
	traveler = models.ManyToManyField(User, related_name='trip')
	destination = models.CharField(max_length=45)
	plan = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
