from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    entry_title = models.CharField(max_length=100)
    entry_text = models.TextField()
    entry_image = models.TextField(max_length=1000)
    entry_date = models.DateTimeField(auto_now=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f'{self.entry_text}'