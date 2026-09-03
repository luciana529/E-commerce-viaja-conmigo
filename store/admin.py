from django.contrib import admin
from .models import Product, ReviewRating, ProductGallery, Favorite
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInLine(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'available_spots', 'category', 'departure_date', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInLine]


admin.site.register(Product, ProductAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
admin.site.register(Favorite)
