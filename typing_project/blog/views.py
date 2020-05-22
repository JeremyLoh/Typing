from django.shortcuts import render

posts = [
    {
        'author': 'Jeremy',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 14 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 15 2020'
    },
]


def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')
