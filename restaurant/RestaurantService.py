from .models import TestRestaurant
import json as json

class RestaurantService:
	# save a new restaurant
	def add_new_restaurant(self):
		try:
			# Add static data to the restaurant
			#Instanciating the model instance
			test_restaurant_instance = TestRestaurant()
			test_restaurant_instance.restaurant_name = 'Thats Y Food'
			test_restaurant_instance.active = 1
			test_restaurant_instance.email_id = 'thatsyfood@gmail.com'
			test_restaurant_instance.phone_number = '04222266554'
			test_restaurant_instance.area = 'Coimbatore'
			test_restaurant_instance.desc = 'Authentic Biriyani'
			test_restaurant_instance.save()
			response_object = self.get_restaurant()
			return json.dumps(response_object)
			
		except Exception as e:
			print e
			
	# get the first restaurant where active = 1
	def get_restaurant(self):
		try:
			response_object = {}
			test_restaurant = TestRestaurant.objects.filter(active = 1)
			if test_restaurant:
				test_restaurant = test_restaurant[0]
				response_object['name'] = test_restaurant.restaurant_name
				response_object['id'] = test_restaurant.id
				response_object['area'] = test_restaurant.area
				response_object['desc'] = test_restaurant.desc
			return response_object
		except TestRestaurant.DoesNotExist:
			return response_object