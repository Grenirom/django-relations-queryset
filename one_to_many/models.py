from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
