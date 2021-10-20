from django.contrib import admin
from django.utils.safestring import mark_safe

from products.forms import ColorModelForm
from products.models import CategoryModel, ProductTagModel, BrandModel, ProductModel, ColorModel, SizeModel, ProductImageModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'visual_color', 'created_at']
    search_fields = ['code']
    list_filter = ['created_at']
    form = ColorModelForm

    def visual_color(self, obj):
        return mark_safe(f'<div style="height:20px; width:20px; background:{obj.code}"></div>')


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'category', 'brand', 'created_at']
    search_fields = ['category', 'brand', 'tags', 'created_at']
    list_filter = ['title', 'short_description']
    autocomplete_fields = ['category', 'brand', 'tags', 'size', 'color']
    readonly_fields = ['real_price']
    inlines = [ProductImageStackedInline]
