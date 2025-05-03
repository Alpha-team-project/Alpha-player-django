from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Author(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="author_profile"
    )
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="author_images", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Music(BaseModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="musics")
    description = models.TextField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    file = models.FileField(upload_to="audio_files", blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="musics"
    )
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="musics"
    )
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)


class Playlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    music = models.ManyToManyField(Music, blank=True, null=True)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="playlist_images", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.user}-{self.title}"
