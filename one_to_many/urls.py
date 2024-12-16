from django.urls import path

from .views import get_products, ProductsListView, ProductDeleteView, ProductPartialUpdateView, ProductCreateView

urlpatterns = [
    # path('products-list/', get_products), # Если вы пишете представления на функциях, вызывать их не нужно
    path('products-list/', ProductsListView.as_view()), # Если вы используете классовые представления, нужно обязательно вызвать метод as_view()
    path('product-delete/<int:pk>/', ProductDeleteView.as_view()),
    path('product-create/', ProductCreateView.as_view()),
    path('product-patrial-update/<int:pk>/', ProductPartialUpdateView.as_view())
]