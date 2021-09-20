from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Khudadad',
        'title': 'First Blog Post',
        'content': 'This is the first post content',
        'date_posted': 'Jan 1, 2021',
    },
    {
        'author': 'Rayan',
        'title': 'Second Blog Post',
        'content': 'This is the second post content',
        'date_posted': 'Feb 12, 2021',
    },
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request,  'blog/about.html', {'title': 'About'})
