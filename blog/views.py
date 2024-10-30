from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


from django.conf import settings
from django.core.mail import send_mail

def home(request):
    context = {'posts' : Post.objects.all() }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name= 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name= 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        user=User.objects.get(username=self.request.user)
        email=user.email
        username=user.username
        subject = 'Your new blog is created'
        message = f'Hi {username}, thank you for using and new content on your profile.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        try:
            send_mail(subject, message, email_from, recipient_list)
            print("mail sent succcessfully")
        except Exception as e:
            print(f"Error sending email: {e}")
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        user=User.objects.get(username=self.request.user)
        email=user.email
        username=user.username
        subject = 'Your blog is updated'
        message = f'Hi {username}, thank you for using and updated your blog.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        try:
            send_mail(subject, message, email_from, recipient_list)
            print("mail sent succcessfully")
        except Exception as e:
            print(f"Error sending email: {e}")
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            user=User.objects.get(username=self.request.user)
            email=user.email
            # postt=Post.objects.get(author=self.request.author)
            # post=postt.title
            username=user.username
            subject=f'your Blog is deleted'
            message=f'Hii Mr.{username} in your blog deleted'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[email,]
            try:
                send_mail(subject, message, email_from, recipient_list)
                print("mail sent succcessfully")
            except Exception as e:
                print(f"Error sending email: {e}")
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html')



from rest_framework import viewsets

from .serializer import Postserializer
class Postviewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=Postserializer
    