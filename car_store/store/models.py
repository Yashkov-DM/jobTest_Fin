from django.db import models
from django.db.models import CASCADE


class Store(models.Model):
    title = models.CharField('Title', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Car store'
        verbose_name_plural = 'Car stores'


class Car(models.Model):
    store = models.ForeignKey(Store, on_delete=CASCADE, related_name='cars')
    title = models.CharField('Title', max_length=50)
    available = models.BooleanField('Available', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cars'
        verbose_name_plural = 'Cars'

