from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'quantity', 'category'] # это то, что будет отображаться при листинге объектов
    list_filter = ['price'] # поля, по которым можно будет проходить фильтром 
    search_fields = ['title'] # поле, по которому мы можем провести поиск по нашим объектам

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)