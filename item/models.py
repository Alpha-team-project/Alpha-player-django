from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# todo: all the models are saved here

# todo: model for Categories
class Category(models.Model):


    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # it ensures are ordered in a natural order by their names
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    # todo: this provides the chance when we call the instance of category, we will get details of instance
    def __str__(self):
        return self.name

# todo: model for Categories
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author_profile')
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='author_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # todo: this provides the chance when we call the instance of category, we will get details of instance
    def __str__(self):
        return self.full_name

# todo: model for Musics
class Music(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='musics')
    description = models.TextField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    file = models.FileField(upload_to='audio_files', blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='musics')
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='musics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    # todo: this provides the chance when we call the instance of category, we will get details of instance
    def __str__(self):
        return self.title

    # todo: this orders musics by created_at
    class Meta:
        ordering = ('-created_at',)