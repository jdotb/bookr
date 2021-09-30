from django.shortcuts import render, get_object_or_404
from .models import Book, Review
from .utils import average_rating

def index(request):
    return render(request, "base.html")

def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "reviews/search-results.html", {"search_text": search_text})

def book_list(request):
    books = Book.objects.all()
    book_list = []

    for book in books:
        reviews = book.review_set.all()

        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)

        else:book_rating = None

        number_of_reviews = 0

        book_list.append({
            'book': book,
            'book_rating': book_rating,
            'number_of_reviews': number_of_reviews})

    context = {
        'book_list': book_list
    }

    return render(request, 'reviews/books_list.html', context)


'''
    Activity 3.01

    Create a book details view that takes a specific book's primary key as the argument 
    and returns an HTML page listing the book's details and any associated reviews.
    
'''
# pk = books (P)rimary (K)ey
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    return render(request, "reviews/book_detail.html", context)