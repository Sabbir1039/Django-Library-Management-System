from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Unknown')
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    # avatar = models.ImageField(upload_to='')

    def __str__(self) -> str:
        return f'{self.name}'


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Mystery', 'Mystery'),
        ('Biography', 'Biography'),
    ]
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50, blank=True)
    publication_year = models.DateField(blank=True, null=True)
    isbn = models.PositiveIntegerField(
        unique=True, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    total_copies = models.PositiveIntegerField(default=0)
    available_copies = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.title}'
