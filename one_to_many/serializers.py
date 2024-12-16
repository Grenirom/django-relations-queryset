from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # ['id', 'title', 'price']

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Цена не может быть отрицательной')
        return price
    
    # есть 2 метода для валидации в сериализаторах, validate, validate_<field>. validate(self, attrs) - attrs - словарь с данными из запроса, сам метод проверяет все данные. validate_<field>(self, <field>) - валидирует какое то определенное поле, все валидация прошла, то нужно обязательно вернуть это поле