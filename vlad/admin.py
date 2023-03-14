from django.contrib import admin
from .models import Currency, User, Parse
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Currency)
admin.site.register(Parse)


