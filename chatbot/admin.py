from django.contrib import admin
from .models import Chat

#Putting the models into the administration site. It's small but interesting
admin.site.register(Chat)