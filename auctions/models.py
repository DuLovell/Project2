from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Advert(models.Model):
	title = models.Charfield(max_length=32)
	#breif_desription = models.Charfield(max_length=64)
	desription = models.TextField(max_length=1024)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	##TODO photo = models.ImageField (разобраться с Pillow)


	def __str__(self):
		return f"{self.id}. {self.title}: {self.desription} | ${self.price}"