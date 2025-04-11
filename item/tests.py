from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from item.models import Category, Author, Music


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Pop")

    def test_category_name_created(self):
        """Test name equal or not"""
        category = Category.objects.get(name="Pop")
        self.assertEqual(category.name, "Pop")


class AuthourTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="johndoe", password="testpassword"
        )

        Author.objects.create(
            user=self.user,
            full_name="John Doe",
            image="./static/images/browse_page.png",
            description="test data",
        )

    def test_author_model_created(self):
        author = Author.objects.get(user=self.user)

        self.assertEqual(author.full_name, "John Doe")
        self.assertEqual(author.image, "./static/images/browse_page.png")
        self.assertEqual(author.description, "test data")


class MusicModelTest(TestCase):
    def setUp(self):
        audio_file = SimpleUploadedFile(
            "./static/YOU.mp3", b"dummy audio content", content_type="audio/mpeg"
        )
        image_file = SimpleUploadedFile(
            "./static/images/browse_page.png", b"image data", content_type="image/jpeg"
        )

        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.author = Author.objects.create(
            user=self.user,
            full_name="John Doe",
            image="./static/images/browse_page.png",
            description="test data",
        )
        self.category = Category.objects.create(name="Pop")
        self.music = Music.objects.create(
            title="Test Song",
            author=self.author,
            category=self.category,
            created_by=self.user,
            image=image_file,
            file=audio_file,
        )

    def test_create_music_basic(self):
        music = Music.objects.create(
            title="Test Song",
            author=self.author,
            category=self.category,
            created_by=self.user,
        )

        self.assertEqual(music.title, "Test Song")
        self.assertEqual(music.category.name, "Pop")
        self.assertEqual(music.created_by.username, "testuser")
        self.assertIsNone(music.length)
        self.assertIsNone(music.description)

    def test_optional_fields(self):
        music = Music.objects.create(
            title="Song With Details",
            author=self.author,
            category=self.category,
            created_by=self.user,
            description="This is a test song",
            length=240,
            lyrics="La la la",
        )

        self.assertEqual(music.description, "This is a test song")
        self.assertEqual(music.length, 240)
        self.assertEqual(music.lyrics, "La la la")

    def test_file_upload(self):
        # Create dummy audio file
        audio_file = SimpleUploadedFile(
            "./static/YOU.mp3", b"dummy audio content", content_type="audio/mpeg"
        )
        image_file = SimpleUploadedFile(
            "./static/images/browse_page.png", b"image data", content_type="image/jpeg"
        )

        music = Music.objects.create(
            title="With Files",
            author=self.author,
            category=self.category,
            created_by=self.user,
            file=audio_file,
            image=image_file,
        )

    def test_soft_delete_field(self):
        music = Music.objects.create(
            title="To Be Deleted",
            author=self.author,
            category=self.category,
            created_by=self.user,
        )
        self.assertIsNone(music.deleted_at)

        # simulate soft delete
        from django.utils import timezone

        music.deleted_at = timezone.now()
        music.save()

        self.assertIsNotNone(music.deleted_at)

    def test_music_detail_view_status_200(self):
        url = f"/items/{self.music.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_music_detail_view_status_301(self):
        url = f"/items/2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

    def test_music_detail_view_status_404(self):
        url_404_1 = f"/items/{self.music.id}/test/url"
        url_404_2 = f"/items/2/"
        
        response_1 = self.client.get(url_404_1)
        response_2 = self.client.get(url_404_2)

        self.assertEqual(response_1.status_code, 404)
        self.assertEqual(response_2.status_code, 404)
