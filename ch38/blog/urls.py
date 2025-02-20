from django.urls import path
from blog.views import blog_post

urlpatterns = [
    path('', blog_post,name='blog_post'),
]
