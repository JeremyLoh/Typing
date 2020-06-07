from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # Modify query set listview returns
    def get_queryset(self):
        # Return 404 error if user does not exist
        # kwargs are query parameters
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


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
    # Set paginator: An integer specifying how many objects should be displayed per page
    paginate_by = 5


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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # After deletion, which page to redirect to
    success_url = '/'
    # Default template name: <model>_confirm_delete.html

    def test_func(self):
        # Check for UserPassesTestMixin
        post = self.get_object()
        return post.author == self.request.user


def about(request):
    return render(request, 'blog/about.html')
