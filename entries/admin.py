from django.contrib import admin
from .models import Entry

#allows one to see the Entry model in the admin site

admin.site.register(Entry)
