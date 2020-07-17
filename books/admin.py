from django.contrib import admin
from .models import Book, Tui, Category, Zcategory, Link, Banner
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'autor', 'tui', 'views', 'created_time')
    list_per_page = 50

    ordering = ('-created_time',)

    list_display_links = ('id', 'name')
@admin.register(Zcategory)
class ZcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display=('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')