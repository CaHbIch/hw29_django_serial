from django.db import models


from ads.models.category import Category
from users.models.user import User


class Ad(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название объявления")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=2000)
    is_published = models.BooleanField(default=None, verbose_name="Публикация")
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-price']

    def __str__(self):
        return self.name