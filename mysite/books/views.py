from django.shortcuts import render
from . models import Book
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  return HttpResponse('Home Page')
#Views in normal format
"""def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books':all_books
    }
    return render(request,'books/index.html',context)
def detail(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("The Book does not exist")
    context ={
        'book':book
    }
    return render(request,'books/detail.html',context)
"""

class Indexview(generic.ListView):
    template_name = "books/index.html"

    def get_queryset(self):
        return Book.objects.all()

class bookcreate(CreateView):
        model = Book
        fields = ['name','author','price','type','book_image']

class Detailview(generic.DetailView):
    model = Book
template_name = 'books/detail.html'