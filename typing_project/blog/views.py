from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


class PostListView(ListView):
    # model to query to create the list
    model = Post
    # Looks for default template of format: <app>/<model>_<viewtype>.html
    # e.g. blog/post_list.html
    template_name = 'blog/index.html'
    # Set variable name to be looped over, default is object_list
    context_object_name = 'posts'
    # Change order of posts (add - to reverse order, default is ascending)
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    # Looks for default template of format: <app>/<model>_<viewtype>.html
    # public key (pk) is used for grabbing object


def about(request):
    return render(request, 'blog/about.html')
