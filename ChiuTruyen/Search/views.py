from django.shortcuts import render
from Book.models import Book


def search(request):
    query = request.GET.get('query')
    books_search_by_name = Book.object.filter(name__icontains=query) if query else []
    books_search_by_alias = Book.object.filter(alias__icontains=query) if query else []
    print(books_search_by_name)
    return render(request, 'searchResult.html', {'query': query,
                                                 'books_search_by_name': books_search_by_name,
                                                 'books_search_by_alias': books_search_by_alias})
