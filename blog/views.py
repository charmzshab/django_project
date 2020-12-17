from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView)
from . models import Post


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # -> <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # -> <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    # returns posts created by a specific user ordered by date
    def get_queryset(self):
        # kwargs is used to get data from the query parameters
        user = get_object_or_404(User,username=self.kwargs.get('username')) # returns a user or a 404 if a user is not found
        return Post.objects.filter(author=user).order_by('-date_posted')


    

class PostDetailView(DetailView):
    model = Post
 
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    # sets the author of the post when creating a new post
    def form_valid(self,form): 
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    # sets the author of the post when creating a new post
    def form_valid(self,form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

    # prevents users that are not authors of the post to update it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

     # prevents users that are not authors of the post to update it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request,'blog/about.html',{'title':'About'})