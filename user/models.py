from django.db import models

# Create your models here.
class user_details(models.Model):

	# Personal Details
	username = models.CharField(max_length=50,default='')
	first_name = models.CharField(max_length=50,default='')
	last_name = models.CharField(max_length=50,default='')
	dob = models.DateField(auto_now=False, auto_now_add=False)
	email = models.EmailField(max_length=254,null=False)
	phone = models.DecimalField(default=0,max_digits=50,decimal_places=0)

	def __str__(self):
		return self.username

	def __unicode__(self):
		return self.username
