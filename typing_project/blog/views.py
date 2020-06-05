from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
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
    # primary key (pk) is used for grabbing object


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # Add fields for form
    fields = ['title', 'content']
    # Shares template with UpdateView
    # Looks for default template <app>/<model>_form.html

    def form_valid(self, form):
        # Set author before submitting form
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # primary key (pk) passed into url route is used for obtaining object
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        # UserPassesTestMixin will run this method
        # Check if User passes test condition
        # Get current post, use UpdateView method
        post = self.get_object()
        return self.request.user == post.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html')
