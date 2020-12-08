from django.db import models

class Portfolio(models.Model):
    objects = None
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    img = models.ImageField(null=True, blank=True, upload_to='static/portfolio')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='portfolio/static/img/gallery')

