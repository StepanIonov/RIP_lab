from django.db import models
from mysite import settings
from django.utils.translation import ugettext_lazy

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ugettext_lazy("Категория")
        verbose_name_plural = ugettext_lazy("Категории")


class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=30, verbose_name="Название")
    structure = models.CharField(max_length=200, verbose_name="Состав")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")
    img = models.ImageField(upload_to='food/images/', default='food/images/No_image_available.jpg', verbose_name="Изображение")
    def __str__(self):
        return 'Название: {}. Состав: {}. Цена: {}.'.format(self.name, self.structure, self.price)
    class Meta:
        verbose_name = ugettext_lazy("Блюдо")
        verbose_name_plural = ugettext_lazy("Блюда")
