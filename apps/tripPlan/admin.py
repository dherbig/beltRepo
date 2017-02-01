from django.contrib import admin
from models import travelPlan
# Register your models here.

class travelPlanAdmin(admin.ModelAdmin):
	pass
admin.site.register(travelPlan, travelPlanAdmin)
