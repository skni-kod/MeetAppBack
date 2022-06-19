from django.contrib import admin

# Register your models here.

from MeetApp.models import *

admin.site.register(Event)

admin.site.register(Profile)

admin.site.register(Profile_Event_Relation)