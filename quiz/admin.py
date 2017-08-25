from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(quiz_short)
admin.site.register(quiz_one)
admin.site.register(quiz_multi)
