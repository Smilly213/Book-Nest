from django.db import models
from django.utils.text import slugify

class Profile(models.Model):
    image = models.ImageField(upload_to='profile/%Y/%m/%d/', verbose_name='Фото')
    full_name = models.CharField(max_length=120, verbose_name='ФИО')
    slug = models.SlugField(verbose_name='Ссылка')
    date = models.DateTimeField(verbose_name='Дата рождения',)
    age = models.IntegerField(verbose_name='Возраст')
    context = models.TextField(verbose_name='О себе')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']