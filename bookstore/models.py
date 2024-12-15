
# Create your models here
from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('other', 'Other'),
    ]

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    cover = models.ImageField(upload_to='book_covers/')
    availability = models.CharField(max_length=10, choices=[('free', 'Free'), ('for_sale', 'For Sale')])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    book_file = models.FileField(upload_to='book_files/')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"
    

class BookRequest(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

