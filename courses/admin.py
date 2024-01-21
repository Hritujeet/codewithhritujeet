from django.contrib import admin
from .models import Tutorial, Course

# Register your models here.
admin.site.register(Course)
@admin.register(Tutorial)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)