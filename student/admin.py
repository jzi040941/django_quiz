from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(SubmitAssign)
admin.site.register(UserProfile)
admin.site.register(SubjectMember)
