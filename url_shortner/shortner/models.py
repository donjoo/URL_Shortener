from django.db import models

class ShortendURL(models.Model):
    original_url = models.URLField(max_length=500)
    short_hash = models.CharField(max_length=10,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.short_hash} -> {self.original_url}'




