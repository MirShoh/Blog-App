from django.contrib import admin
from .models import Article, Comment

class CommentLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentLine]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)