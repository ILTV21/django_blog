from django.db import models
from datetime import date
# from django.urls import reverse
# from django.utils.text import slugify
from django.core.validators import MinLengthValidator



class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email_field = models.EmailField(max_length=242)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Authors"

class Post(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True, blank=True, null=True)
    slug = models.SlugField(unique=True, default="", blank = True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return f"{self.title} {self.author.first_name}"


    
# Create your models here.
