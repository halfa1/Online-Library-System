# Online Library Project

## Overview

This project is a simple **Django-based Online Library** where users can upload, download, request and review books. It provides functionality for managing softcopy books.

---

## Features

1. **User Uploads:**
   - Users can upload digital books (PDFs) along with cover images.
   - Users can provide details like title, author, category, price, and publication date.
2. **Book Browsing:**

   - Users can browse available books with detailed information.
   - Free books are available for download, while others are marked as "Coming Soon."

3. **Reviews:**

   - Users can leave reviews with ratings for any book.
   - Reviews are displayed alongside the book details.

4. **Categories:**

   - Books can be categorized for easy browsing.

5. **Hardcopy Books:**
   - Hardcopy book information, including cover images, is also stored and displayed.

---

## Requirements

- **Python**: 3.8+
- **Django**: 4.x
- **Bootstrap**: Used for styling.
- **Database**: SQLite (default for development).

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd online_library
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Project Structure

```
online_library/
├── bookstore/         # Main app for books and reviews
├── media/             # Uploaded media (book covers and files)
├── static/            # Static assets (CSS, JS, etc.)
├── templates/         # HTML templates
├── db.sqlite3         # SQLite database
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

---

## Key Files

1. **Forms:**

   - `forms.py`: Contains `BookUploadForm` and `ReviewForm`.

2. **Models:**

   - `models.py`: Defines `Book` and `Review` models.

3. **Views:**

   - `views.py`: Manages book upload, display, and review submission.

4. **Templates:**
   - `upload_book.html`: Template for book uploads.
   - `book_detail.html`: Template to display book details and reviews.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

---

## License

This project is open-source and available under halfamaton

---

Happy coding!
