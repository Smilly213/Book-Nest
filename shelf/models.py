from django.db import models
from users.models import Profile
from books.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator

class Status(models.IntegerChoices):
    not_started = (0, "В планах")
    reading = (1, 'Читаю')
    finished = (2, 'Прочитано')

class Shelf(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='shelf_entries')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='shelf_entries')
    status = models.IntegerField(choices=Status.choices, default=Status.not_started)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=None, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user} — {self.book} ({self.get_status_display()})'
