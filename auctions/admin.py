from django.contrib import admin
from .models import User, Advert, Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Advert)
admin.site.register(Bid)
admin.site.register(Comment)
