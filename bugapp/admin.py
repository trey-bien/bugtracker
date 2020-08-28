from django.contrib import admin

from bugapp.models import MyUser, Ticket

admin.site.register(MyUser)
admin.site.register(Ticket)
