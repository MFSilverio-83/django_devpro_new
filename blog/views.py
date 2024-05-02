from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post # do arquivo models, importe a tabela post
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def post_list(request):
    # na linha abaixo serão gravados os post de acordo com data de publicação
    # posts será uma nova variável criada, que pode ser utilizada em outro local (templates)
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # o filtro acima significa ordernar por data <= timezone de agora (__lte) de forma decrescente (-)
    paginator = Paginator(posts_list, 5)  # Define o número de posts por página
    page_number = request.GET.get('page')  # Obtém o número da página da query string, que está no navegador
    posts = paginator.get_page(page_number)  # Obtém os posts para a página atual
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)      # antes de salvar na tabela
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)  # pegando as informações do post que já existe
        if form.is_valid():
            post = form.save(commit=False)    # abrindo a edição no banco sem salvar
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    # garante que pegamos apenas postagens não publicadas e por ordem de criação
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
     post = get_object_or_404(Post, pk=pk)
     post.delete()
     return redirect('post_list')

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'blog/login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('post_list')