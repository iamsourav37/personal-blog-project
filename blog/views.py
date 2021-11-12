from django.shortcuts import render, HttpResponse
from .models import Category, Post
# Create your views here.


def index(request):
    category = Category.objects.all()
    posts = Post.objects.all()
    data = {
        "category": category,
        "posts": posts
    }
    return render(request, "home.html", data)


def category_wise_post(request, category_name):
    category_id = Category.objects.get(title=category_name)
    category = Category.objects.all()
    filtered_posts = Post.objects.filter(category=category_id)

    data = {
        "posts": filtered_posts,
        "category": category,
    }
    return render(request, "category_wise_post.html", data)


def specific_post(request, url):
    post = Post.objects.get(url=url)
    category = Category.objects.all()
    popular_posts = Post.objects.all()
    data = {
        "post": post,
        "category": category,
        "popular_post": popular_posts,
    }
    return render(request, "post_details.html", data)
