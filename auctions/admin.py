from django.contrib import admin
from .models import User, Advert, Bid

# Register your models here.
admin.site.register(User)
admin.site.register(Advert)
admin.site.register(Bid)