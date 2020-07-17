from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import *
from .forms import *
import uuid



def home(request):
    categories = Category.objects.all()
    post = Post.objects.all()[0]
    posts_all = Post.objects.all()
    recent_post = Post.objects.all()[0:5]

    paginator = Paginator(posts_all, 4)
    page_number = request.GET.get('page')
    posts_all = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'post': post,
        'posts_all': posts_all,
        'recent_post': recent_post
    }
    return render(request, 'blog/home.html', context)



def recent_posts(request):
    posts = Post.objects.all()[0:10]
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/recent_posts.html', context)


def detail_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    categories = Category.objects.all()
    context = {
        'post': post,
        'categories': categories
    }
    return render(request, 'blog/detail_post.html', context)


def posts_under_category(request, cat_id):
    category = Category.objects.get(pk=cat_id)
    posts = category.post_set.all()
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'blog/posts_under_category.html', context)


def create_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            form.save()
            messages.info(request, f"Category '{title}' added successfully !")
            return HttpResponseRedirect(reverse('Blog_app:home'))

    context = {
        'form': form
    }
    return render(request, 'blog/create_category.html', context)



def create_post(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post_obj = form.save(commit=False)
            post_obj.author = request.user
            title = post_obj.title
            post_obj.post_slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
            post_obj.save()

            return HttpResponseRedirect(reverse('Blog_app:home'))


    context = {
        'form': form
    }
    return render(request, 'blog/create_post.html', context)



