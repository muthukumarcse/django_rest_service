# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
import json as json
from django.conf import settings
from .models import TestRestaurant
from .RestaurantService import RestaurantService

# function based view
@api_view(['POST'])
def add_restaurant(request):
	try:
		# Instanciating Restaurant Service object
		restaurant_service = RestaurantService()
		return HttpResponse(restaurant_service.add_new_restaurant(), mimetype='application/json')
	except Exception as e:
		print e
	