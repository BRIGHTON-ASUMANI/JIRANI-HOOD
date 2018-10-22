from django.contrib import admin
from .models import  Neighbourhood, Profile, Business

admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)
