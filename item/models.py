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
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="playlist_images", blank=True, null=True)

    def __str__(self):
        return f"{self.name} by {self.user.username}"


class PlaylistMusic(models.Model):
    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, related_name="playlist_musics"
    )
    music = models.ManyToManyField(Music)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        # unique_together = ('playlist', 'music')
        ordering = ["order"]

    def __str__(self):
        return f"{self.playlist.name}"
