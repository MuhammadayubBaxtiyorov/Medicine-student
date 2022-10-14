from django.contrib import admin
from .models import Medicine, Times, NotificationPerson
# Register your models here.

admin.site.register(Medicine)
admin.site.register(Times)
admin.site.register(NotificationPerson)
