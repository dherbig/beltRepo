from django import forms
from .models import travelPlan
from django.contrib import messages
from datetime import date

class AddTrip(forms.ModelForm):
	# Since most of this form is assembled automatically using ModelForm tricks, these first two lines format the start and end date fields to use the date picker widget. ^_^

	start_date=forms.DateField(widget=forms.SelectDateWidget())
	end_date=forms.DateField(widget=forms.SelectDateWidget())
	# This section looks at the travelPlan model and makes fields for each of the stated values.
	class Meta:
		model = travelPlan
		fields = ['destination', 'plan', 'start_date', 'end_date']

	# This overrides (and includes) the ModelForm's clean function, which validates data, so that I can check to make sure all the dates are in the future, and that the start_date comes before the end_date
	def clean(self):
		# This runs the inheritied .clean()
		cleaned_data = super(AddTrip, self).clean()

		# Snags the start_date
		start = cleaned_data.get("start_date")
		# Snags the end_date
		end = cleaned_data.get("end_date")

		# Checks to see if the start comes after the end.
		if start > end or start < date.today():
			raise forms.ValidationError("The End Comes Before The Beginning!")
			messages.error(request, "Trip lasts negative days.")
			print('We just put up an error message...')
		# Now, when we run .clean() on registration forms, it will also check to make sure the start and end times make sense.
		return self.cleaned_data
