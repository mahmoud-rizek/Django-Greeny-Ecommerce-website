from .serializers import ProductSerializer, CategorySerializer, BrandSerializer, productReviewsSerializer
from .models import product, Category, Brand, productReviews
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets

 # Functions API


# Generics class API
class ProductListAPI(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPI(generics.RetrieveAPIView ):
    queryset = product
    serializer_class = ProductSerializer


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPI(generics.RetrieveAPIView):
    queryset = Category
    serializer_class = CategorySerializer


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = CategorySerializer

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand
    serializer_class = BrandSerializer



class ProductReviewsList(generics.ListAPIView):
    queryset = productReviews.objects.all()
    serializer_class = productReviewsSerializer


# Viewsets API
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = product.objects.all()