from django.db import models

# Create your models here.
class TestRestaurant (models.Model):
	restaurant_name		             = models.CharField(max_length=45 , null=False)
	active			                 = models.BooleanField(null=False , default=True)
	email_id						 = models.EmailField(max_length=70)
	phone_number					 = models.CharField(max_length=15)
	area							 = models.CharField(max_length=45)
	desc							 = models.CharField(max_length=45)

	def __unicode__(self):
		return self.restaurant_name
    
	class Meta:
		db_table = 'test_restaurant'