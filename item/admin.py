from django.contrib import admin

from .models import Category, Music, Author, Playlist

admin.site.register(Category)
admin.site.register(Music)
admin.site.register(Author)
admin.site.register(Playlist)
