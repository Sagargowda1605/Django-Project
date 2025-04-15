from django.contrib import admin
from .models import Room,Topic,Messages,Profile

# Register your models here.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Messages)
admin.site.register(Profile)
