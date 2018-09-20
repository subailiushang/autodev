from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Projects, Tickets, MyUser


admin.site.register(Projects)
admin.site.register(Tickets)
admin.site.register(MyUser, UserAdmin)
