from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="books/profile_images", null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):

        return f'{self.first_name} {self.last_name}'