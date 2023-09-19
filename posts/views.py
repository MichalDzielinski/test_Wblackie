from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    p = Post.objects.all()
    context = {'p':p}
    return render(request, 'posts/index.html', context)