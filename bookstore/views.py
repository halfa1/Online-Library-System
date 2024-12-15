#create your views here
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .forms import BookUploadForm, ReviewForm, RequestBookForm
from django.core.mail import send_mail

@login_required
def booklists(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    category = request.GET.get('category')

    if query:
        books = books.filter(title__icontains=query)

    if category:
        books = books.filter(category=category)

    categories = Book.objects.values('category').distinct()  # Get distinct categories for filtering
    return render(request, "bookstore/index.html", {"books": books, "categories": categories})

@login_required
def book_details(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been added!")
            return redirect('bookstore:book_details', book_id=book.id)

    return render(request, "bookstore/book_details.html", {"book": book, "reviews": reviews, "form": form})

@login_required
def upload_book(request):
    if request.method == "POST":
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploaded_by = request.user  # Make sure you’re saving the user
            book.save()
            messages.success(request, "Book uploaded successfully!")
            return render(request, 'bookstore/upload_success.html')  # Success page 
        else:
            # If form is invalid, print errors for debugging
            print(form.errors)
            messages.error(request, "There was an error uploading your book. Please check the form fields.")
    else:
        form = BookUploadForm()

    return render(request, "bookstore/upload_book.html", {"form": form})




@login_required
def request_book(request):
    if request.method == 'POST':
        form = RequestBookForm(request.POST)
        if form.is_valid():
            book_request = form.save()  # Save to the database

            # Send email to admin
            send_mail(
                f"Book Request: {book_request.title}",
                f"Requested by: {book_request.email}\nAuthor: {book_request.author}\nMessage: {book_request.message}",
                'admin@yourdomain.com',  # Replace with your admin email
                ['admin@yourdomain.com']  # Replace with your admin email
            )

            # Send automated reply
            send_mail(
                "Book Request Received",
                "Thank you for your request. Please check back for updates.",
                'noreply@yourdomain.com',  # Replace with your noreply email
                [book_request.email]
            )

            return render(request, 'bookstore/request_success.html')  # Success page
    else:
        form = RequestBookForm()

    return render(request, 'bookstore/request_book.html', {'form': form})

