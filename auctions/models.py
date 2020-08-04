from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass




class Advert(models.Model):
	title = models.CharField(max_length=32)
	description = models.TextField(max_length=1024)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)

	##TODO photo = models.ImageField (разобраться с Pillow)
	#breif_desription = models.Charfield(max_length=64)

	def __str__(self):
		return f"{self.id}. {self.title}: {self.description}"


class Bid(models.Model):
	user = models.CharField(max_length=32)
	amount = models.DecimalField(max_digits=8, decimal_places=2)
	advertisement = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name="bid")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user}: {self.amount}"

class Comment(models.Model):
	user = models.CharField(max_length=32)
	text = models.CharField(max_length=64)
	advertisement = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name="comments")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user}: {self.text}"