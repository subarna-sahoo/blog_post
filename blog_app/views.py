from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# def home(request):
#     context = {
#         'posts': post.objects.all()

#     }
#     return render(request, 'blog_app/home.html', context)


class PostListView(ListView):
    posts = post.objects.all()
    model = post
    template_name = 'blog_app/home.html'  # <app>/<model>_<view-type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # newer blogs are first
    paginate_by = 5


class UserPostListView(ListView):
    posts = post.objects.all()
    model = post
    template_name = 'blog_app/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    # for author link to access and filter the post of the respective author name
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = post
    # newer blogs are first


class PostCreateView(LoginRequiredMixin, CreateView):
    # loginrequiremixin is used for user have to creat a accaunt before see the post
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        # for create the post acc to the current log in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # loginrequiremixin is used for user have to creat a accaunt before see the post
    # UserPassesTestMixin is used for preventing user to update anyothers posts
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        # for create the post acc to the current log in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ''' preventing user to update others posts   '''
        post = self.get_object()  # to get the post
        if self.request.user == post.author:
            # curent log in user == author of the post
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        ''' preventing user to update others posts   '''
        post = self.get_object()  # to get the post
        if self.request.user == post.author:
            # curent log in user == author of the post
            return True
        return False


def about(request):
    return render(request, 'blog_app/about.html', {'title': 'about'})
