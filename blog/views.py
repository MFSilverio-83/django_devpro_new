from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def portao(request):
    return HttpResponse ("Você chegou no portão!")

def post_list(request):
    return render(request, 'blog/post_list.html', {})