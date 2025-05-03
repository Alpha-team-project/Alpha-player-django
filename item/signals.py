from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Playlist


@receiver(post_save, sender=User)
def create_default_playlists(sender, instance, created, **kwargs):
    if created:
        Playlist.objects.bulk_create(
            [
                Playlist(
                    user=instance,
                    name="Favorites",
                    description="Your favorite songs",
                    order=0,
                ),
                Playlist(
                    user=instance,
                    name="See Later",
                    description="Songs to check out later",
                    order=0,
                ),
                Playlist(
                    user=instance,
                    name="Chill Vibes",
                    description="Relaxing and calm music",
                    order=0,
                ),
            ]
        )
