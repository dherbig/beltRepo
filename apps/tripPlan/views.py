from django.shortcuts import render, redirect
from .models import travelPlan
from ..loginReg.models import User
from .forms import AddTrip
from django.contrib import messages
# Create your views here.
def index(request):
	context = {}
	context['user'] = User.objects.get(id=request.session['user_id'])
	context['upcomingTrips'] = travelPlan.objects.filter(traveler=context['user'])
	context['otherTrips'] = travelPlan.objects.exclude(traveler=context['user'])
	manyManager = travelPlan.objects.get(id=1)
	print('--------------------------------------')
	print(manyManager.traveler)
	print('--------------------------------------')
	return render(request, 'tripPlan/index.html', context)

def addTrip(request):
	# If you're not logged in...
	if not 'user_id' in request.session:
		# Then you shouldn't be here!  Move along!
		return redirect('loginReg:index')
	context = {}
	context['user'] = User.objects.get(id=request.session['user_id'])
	print(context['user'])
	context['addTrip'] = AddTrip()
	return render(request, 'tripPlan/add.html', context)

# Adds a new travelPlan to the database, and registers the logged in user to it.
def confirm(request):
	# Stores the form's data
	bound_form = AddTrip(request.POST)
	print(bound_form)
	theTraveler = User.objects.get(id=request.session['user_id'])
	print(theTraveler)
	# Checks the data integrity using the guidelines in forms.py
	if bound_form.is_valid():
		# Saves the data to a new travelPlan object
		bound_form = bound_form.save()
		# We're done here.  Lets go back to the index.
		bound_form.traveler.add(theTraveler)
		bound_form.save()
		print('-------------------------')
		print(bound_form.traveler)
		print('-------------------------')
		print(bound_form.traveler)
		print("That shoulda worked.  Go check.")
		return redirect('tP:index')
	else:
		# Something has gone wrong!
		print("THIS TRIP IS RUINED!")
		messages.error(request, 'Trip registration failed. Try again.')
		# Go back to addTrip to try again.
		return redirect('tP:addTrip')

def tripInfo(request, id):
	context = {}
	context['theTrip'] = travelPlan.objects.get(id=id)
	print (context['theTrip'].traveler)
	return render(request, 'tripPlan/tripInfo.html', context)

def joinTrip(request, id):
	theTraveler = User.objects.get(id=request.session['user_id'])
	theTrip = travelPlan.objects.get(id=id)
	theTrip.traveler.add(theTraveler)
	theTrip.save()
	return redirect('tP:index')
