from django.shortcuts import render
from blog.forms import CreatePostForm

# Create your views here.
def blog_post(request):
    form = CreatePostForm()
    return render(request,'blog/home.html', {'form':form})