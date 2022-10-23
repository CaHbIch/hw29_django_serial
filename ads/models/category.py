from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
