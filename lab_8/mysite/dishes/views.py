from django.shortcuts import get_object_or_404, render
from .models import Dish, Description


def index(request):
    dish_list = Dish.objects.order_by('name')[:3]
    context = {
        'dish_list': dish_list,
    }
    return render(request, 'dishes/index.html', context)


def detail(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    description = get_object_or_404(Description, pk=dish)
    return render(request, 'dishes/detail.html', {'dish': dish, 'description': description})