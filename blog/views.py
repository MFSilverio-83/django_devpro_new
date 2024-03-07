from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post # do arquivo models, importe a tabela post
# Create your views here.

def post_list(request):
    # na linha abaixo serão gravados os post de acordo com data de publicação
    # posts será uma nova variável criada, que pode ser utilizada em outro local (templates)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})





