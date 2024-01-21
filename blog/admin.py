from django.contrib import admin
from blog.models import Post, Comment

admin.site.register(Comment)
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)