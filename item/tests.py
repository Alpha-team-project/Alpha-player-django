from django.test import TestCase
from django.contrib.auth.models import User
from item.models import Category, Author, Music

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Pop")

    def test_category_name_created(self):
        """Test name equal or not"""
        category = Category.objects.get(name="Pop")
        self.assertEqual(category.name, 'Pop')

class AuthourTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='johndoe', password='testpassword')

        Author.objects.create(
            user=self.user, full_name="John Doe",
            image="./static/images/browse_page.png",
            description="test data")

    def test_author_model_created(self):
        author = Author.objects.get(user=self.user)

        self.assertEqual(author.full_name, "John Doe")
        self.assertEqual(author.image, "./static/images/browse_page.png")
        self.assertEqual(author.description, "test data")
       
