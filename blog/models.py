from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import format_html
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/category")
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def image_tag(self):
        return format_html(f"<img src='{self.image.url}' height='60' width='60' style='border-radius:50%;' >")


class Post(models.Model):
    title = models.CharField(max_length=140)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    content = RichTextField(default="")
    image = models.ImageField(upload_to="media/post")
    url = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def image_tag(self):
        return format_html(f"<img src='{self.image.url}' height='60' width='60' style='border-radius:50%;' >")
