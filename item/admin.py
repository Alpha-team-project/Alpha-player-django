from django.contrib import admin

from .models import Category, Music, Author

admin.site.register(Category)
admin.site.register(Music)
admin.site.register(Author)