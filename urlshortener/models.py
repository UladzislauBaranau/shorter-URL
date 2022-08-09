from django.contrib.auth.models import User
from django.db import models


class Urls(models.Model):
    origin_url = models.URLField()
    short_id = models.SlugField(max_length=6, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.origin_url} - {self.short_id}"

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs list'
        ordering = ['-pub_date']
