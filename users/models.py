from django.db import models
from django.utils.text import slugify
from datetime import date

class Profile(models.Model):
    image = models.ImageField(upload_to='profile/%Y/%m/%d/', verbose_name='Фото')
    full_name = models.CharField(max_length=120, verbose_name='ФИО')
    slug = models.SlugField(blank=True, unique=True, allow_unicode=True, verbose_name='Ссылка')
    birth_date = models.DateField(verbose_name='Дата рождения')
    context = models.TextField(verbose_name='О себе')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.pk:
            base_slug = slugify(self.full_name, allow_unicode=True)
            slug = base_slug
            counter = 1
            while Profile.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    class Meta:
        ordering = ['-birth_date']