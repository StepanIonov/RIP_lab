from django.contrib import admin
from .models import Category, Dish
from django.utils.safestring import mark_safe
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.html import format_html


class DishAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("name", "structure", "price", "preview", )
    list_filter = ("category", )
    search_fields = ("name__startswith", )
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" height="100">')
    preview.short_description = "Превью"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "view_dishes_link")

    def view_dishes_link(self, obj):
        count = obj.dish_set.count()
        url = (
            reverse("admin:food_dish_changelist")
            + "?"
            + urlencode({"category": f"{obj.id}"})
        )
        return format_html('<a href="{}">Количество блюд: {}</a>', url, count)
    
    view_dishes_link.short_description = "Блюда"

 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)

