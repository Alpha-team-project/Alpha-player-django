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
                    title="Favorites",
                    description="Your favorite songs",
                    image="images/favourite.png",
                    order=1,
                ),
                Playlist(
                    user=instance,
                    title="See Later",
                    description="Songs to check out later",
                    image="images/see-you-later.jpg",
                    order=2,
                ),
                Playlist(
                    user=instance,
                    title="Chill Vibes",
                    description="Relaxing and calm music",
                    image="images/chill-vibes.jpg",
                    order=3,
                ),
            ]
        )
