from django.contrib import admin
from .models import Profile,firstname,lastname,username,password


# Register your models here.
admin.site.register(profile)
admin.site.register(firstname)
admin.site.register(lastname)
admin.site.register(username)
admin.site.register(password)
admin.site.register(dob)
