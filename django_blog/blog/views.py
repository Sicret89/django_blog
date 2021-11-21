from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_message = "Your post has been Created!"

    def update(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostUpdateView, self).update(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_message = "Your post has been Updated!"

    def update(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostUpdateView, self).update(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    success_url = '/'
    success_message = "Your post has been Deleted!"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
