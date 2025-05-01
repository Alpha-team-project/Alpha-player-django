from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Category, Author, Music, Playlist
from .forms import MusicForm, CategoryForm, AuthorForm
from django.db.models import Q


# Category Views
def category_list(request):
    categories = Category.objects.all()
    query = request.GET.get("query", "")
    if query:
        categories = categories.filter(name__icontains=query)
    return render(
        request,
        "item/items.html",
        {
            "categories": categories,
            "query": query,
        },
    )


@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("item:category_list")
    else:
        form = CategoryForm()
    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "New Category",
        },
    )


@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("item:category_list")
    else:
        form = CategoryForm(instance=category)
    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "Edit Category",
        },
    )


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("item:category_list")


# Author Views
@login_required
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    music_list = Music.objects.filter(author=author, deleted_at__isnull=True)
    return render(
        request,
        "item/detail.html",
        {
            "author": author,
            "music_list": music_list,
        },
    )


@login_required
def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user  # Tie author to current user
            author.save()
            return redirect("item:author_detail", pk=author.pk)
    else:
        form = AuthorForm()
    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "New Author Profile",
        },
    )


@login_required
def author_edit(request, pk):
    author = get_object_or_404(
        Author, pk=pk, user=request.user
    )  # Only allow editing own profile
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect("item:author_detail", pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "Edit Author Profile",
        },
    )


# Music Views
def music_list(request):
    query = request.GET.get("query", "")
    items = Music.objects.filter(deleted_at__isnull=True)  # Show only non-deleted music
    categories = Category.objects.all()
    category_id = request.GET.get("category", 0)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    return render(
        request,
        "item/items.html",
        {
            "items": items,
            "query": query,
            "categories": categories,
            "category_id": int(category_id),
        },
    )


def music_detail(request, pk):
    item = get_object_or_404(Music, pk=pk)
    related_items = Music.objects.filter(
        category=item.category, deleted_at__isnull=True
    ).exclude(pk=pk)[:3]
    return render(
        request,
        "item/detail.html",
        {
            "item": item,
            "related_items": related_items,
        },
    )


@login_required
def music_new(request):
    if request.method == "POST":
        form = MusicForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            music = form.save(commit=False)
            music.created_by = request.user
            music.save()
            return redirect("item:music_detail", pk=music.pk)
    else:
        form = MusicForm(user=request.user)
    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "New Music",
        },
    )


@login_required
def music_edit(request, pk):
    item = get_object_or_404(Music, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = MusicForm(request.POST, request.FILES, instance=item, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("item:music_detail", pk=item.pk)
    else:
        form = MusicForm(instance=item, user=request.user)
    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "Edit Music",
        },
    )


@login_required
def music_delete(request, pk):
    item = get_object_or_404(Music, pk=pk, created_by=request.user)
    item.deleted_at = timezone.now()
    item.save()
    return redirect("item:music_list")


@login_required
def playlist(request):
    playlists = Playlist.objects.filter(user=request.user)[0:20]
    return render(
        request,
        "item/playlist.html",
        {
            "playlists": playlists,
        },
    )


@login_required
def playlist_detail(request, pk):
    playlist_details = get_object_or_404(Playlist, user=request.user, pk=pk)
    print("-------------------------------------")
    print("-------------------------------------", playlist_details.music.all())
    print("-------------------------------------")
    return render(
        request,
        "item/playlist_detail.html",
        {
            "playlist_detail": playlist_details.music.all(),
        },
    )


@login_required
def add_to_playlist(request):
    if request.method == "POST":
        music_id = request.POST.get("music_id")
        playlist = request.POST.get("playlist_id")
        music = get_object_or_404(Music, id=music_id)
        playlist = get_object_or_404(Playlist, id=playlist, user=request.user)

        playlist.music.add(music)

        return redirect("item:music_detail", pk=1)
