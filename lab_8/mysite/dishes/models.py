from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Description(models.Model):
    dish = models.OneToOneField(Dish, on_delete=models.CASCADE, primary_key=True)
    structure = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    def __str__(self):
        return 'Состав: {structure}. Цена: {price}'.format(structure=self.structure, price=self.price)