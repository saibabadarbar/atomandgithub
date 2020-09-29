from django.contrib import admin
from myapp.models import Devotee

class DevoteeAdmin(admin.ModelAdmin):
    list_display=['name','email','Feedback']
admin.site.register(Devotee,DevoteeAdmin)
