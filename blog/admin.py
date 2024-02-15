from django.contrib import admin
from .models import Post

# admin.site.register(Post) - esta é a forma padrão de registro de usuários

# na forma abaixo, é usado um decorator, e uma classe que permite diferente visualização
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ("author", "title", "text", "created_date", "published_date")

