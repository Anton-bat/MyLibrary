from django.shortcuts import render
from authors.models import Author
from django.http import HttpResponse
# Create your views here.

def index(request):
    authors = Author.objects.all()
    context = {'authors': authors, 'title': 'list of Authors'}
    return render(request, 'authors/authors_list.html', context)

def test(request):
    return HttpResponse('Test')