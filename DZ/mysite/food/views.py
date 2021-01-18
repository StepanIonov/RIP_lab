from django.shortcuts import render
from .models import Category, Dish
from django.http import Http404


def index(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'food/index.html', context)


def dish(request, category_id):
    category = Category.objects.get(pk=category_id)
    category_list = Category.objects.all()
    context = {'category': category, 'category_list': category_list}
    return render(request, "food/dish.html", context)