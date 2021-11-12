from django.urls import path
from .views import index, category_wise_post, specific_post


urlpatterns = [
    path("", index, name="home"),
    path("category/<str:category_name>", category_wise_post, name="category"),
    path("post/<slug:url>", specific_post, name="post"),
]