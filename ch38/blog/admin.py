from django.contrib import admin
from blog.models import Blog_Post

# Register your models here.
@admin.register(Blog_Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content']
