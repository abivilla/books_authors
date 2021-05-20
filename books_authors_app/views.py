from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        "all_books":Book.objects.all()
    }
    return render (request,'index.html',context)

def add_book(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST["title"],desc=request.POST["desc"])
    return redirect('/')

def author(request):
    context = {
        "all_authors":Author.objects.all()
    }
    return render (request,'authors.html', context)

def add_author(request):
    if request.method == "POST":
        Author.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],notes=request.POST["notes"])
    return redirect('/authors')

def book_desc(request,id):
    book=Book.objects.get(id=id)
    if request.method == "GET":
        context = {
        "book":book,
        "author":Author.objects.all()
    }
        return render(request,'book_desc.html',context)
    else:
        link_id =request.POST["link_author"]
        author = Author.objects.get(id=link_id)
        book.authors.add(author)
        return redirect('/')

def author_desc(request,id):
    author=Author.objects.get(id=id)
    if request.method == "GET":
        context = {
        "book":Book.objects.all(),
        "author":author
    }
        return render(request,'author_desc.html',context)
    else:
        link_id =request.POST["link_book"]
        book = Book.objects.get(id=link_id)
        author.books.add(book)
        return redirect('/authors')