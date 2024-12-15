from django import forms
from .models import Book,Review,BookRequest

# Define category choices outside the class
CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('other', 'Other'),
    ]


class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'category', 'cover', 'book_file', 'price', 'availability']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author\'s name'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'category': forms.Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-control'}),  # Use the CATEGORY_CHOICES here
            'cover': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'book_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),  # Make it a dropdown instead of checkbox
        }





class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']


class RequestBookForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ['title', 'author', 'email', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the author\'s name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter additional details'}),
        }

