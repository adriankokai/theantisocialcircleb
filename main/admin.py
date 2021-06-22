from django.contrib import admin
from .models import EmailList
from .models import Application

# Register your models here.
admin.site.register(EmailList)
admin.site.register(Application)

