from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# FBV - Function Based Views, предcтавления, которые написаны на функциях
# CBV - Class Based Views, те же представления, но на классах

def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = []
        for product in products:
            data.append({
                'id': product.id,
                'title': product.title,
                'price': product.price,
                'description': product.description,
                'quantity': product.quantity,
                'category': product.category.name
            })
        return JsonResponse(data, safe=False)
    
# APIView - класс, который позволяет нам писать представления на классах
class ProductsListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # is_valid() - метод, который запускает валидации сериализатора
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductDeleteView(APIView):
    def delete(self, request, pk):
        product = Product.objects.filter(pk=pk).first()
        if not product:
            return Response({'msg': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'msg': 'Товар удален'}, status=status.HTTP_204_NO_CONTENT)


class ProductPartialUpdateView(APIView):
    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'msg': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    