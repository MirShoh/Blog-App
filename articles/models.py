from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Article(models.Model):
    maqola_nomi = models.CharField(max_length=255)
    qisqacha = models.CharField(max_length=200, blank=True)
    matni = RichTextField()
    rasmi = models.ImageField(upload_to="images/", blank=True)
    sanasi = models.DateTimeField(auto_now_add=True)
    muallifi = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.maqola_nomi

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')