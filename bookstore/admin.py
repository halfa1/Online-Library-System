#register your models here

from django.contrib import admin
from .models import Book, BookRequest, Review
class BookAdmin(admin.ModelAdmin):
    exclude = ('uploaded_by',)  # Hide 'uploaded_by' field from the admin form

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)

    list_display = ('title', 'author', 'publication_date', 'category', 'availability', 'price', 'book_file')
    list_filter = ('category', 'availability')
    search_fields = ('title', 'author')
    fields = ('title', 'author', 'publication_date', 'category', 'cover', 'availability', 'price', 'book_file')


class BookRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'email', 'requested_at')
    search_fields = ('title', 'author', 'email')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('book_title', 'user')

admin.site.register(Book, BookAdmin)
admin.site.register(BookRequest, BookRequestAdmin)
admin.site.register(Review, ReviewAdmin)