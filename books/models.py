from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import Profile
from django.utils.text import slugify
from django.urls import reverse

class Book(models.Model):
    image = models.ImageField(upload_to='cover/%Y/%m/%d/', verbose_name='Обложка')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)
    genre = models.ManyToManyField('Genre', related_name='books', verbose_name='Жанры')
    author = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='books', verbose_name='Автор')
    date = models.DateTimeField(auto_now_add=True)
    context = models.TextField(verbose_name='Описание')
    file = models.FileField(
        upload_to='books/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'epub', 'fb2'])],
        verbose_name='Файл книги'
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title, allow_unicode=True)
            slug = base_slug
            count = 1
            while Book.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail_book', kwargs={'book_slug': self.slug})

class Genre(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, allow_unicode=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)