from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

posts = [
    {
        'author': 'carti',
        'songname': '@ meh',
        'genre': 'mumble'
    },
    {
        'author':'uzi',
        'songname':'chrome heart tags',
        'genre':'mumble'
    }

]

# Create your views here.
def home(requests):
    title = 'HelloWorld'

    context = {
        'posts': Post.objects.all()
    }

    return render(requests, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title':'aboutawdawdawd'})