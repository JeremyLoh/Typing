from . import views
from django.urls import path
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-index"),
    path('about/', views.about, name="blog-about")
]
