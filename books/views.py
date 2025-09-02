from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Book
from .forms import BookCreateForm


@require_http_methods(['GET'])
def book_list(request):
    book_list = Book.objects.all()
    form = BookCreateForm(auto_id=False)
    return render(request, 'base.html', {'book_list': book_list}, 'form': form)

@require_http_methods(['POST'])
def book_list(request):
    form = BookCreateForm(request.POST)
    if form.is_valid():
        book = form.save()
    return render(request, 'partial_book_detail.html', {'book': book})