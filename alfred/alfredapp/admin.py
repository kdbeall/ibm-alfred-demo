from django.contrib import admin
from .models import User, ItemRequest
# Register your models here.
admin.site.register(User)
admin.site.register(ItemRequest)

admin.site.site_header = 'Alfred Administration'
