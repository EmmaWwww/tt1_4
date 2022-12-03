from django.contrib import admin

# Register your models here.

from .models import Transaction

#can access: http://127.0.0.1/admin/ (tell django which table defined in models.py, the superuser will access & to edit data to db)
admin.site.register(Transaction)

