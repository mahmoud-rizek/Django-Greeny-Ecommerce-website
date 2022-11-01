from .serializers import ProductSerializer, CategorySerializer, CategoryDetailSerializer, BrandSerializer, BrandDetailSerializer,productReviewsSerializer, productDetailSerializer
from .models import product, Category, Brand, productReviews
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .pagination import myPagination
from django_filters.rest_framework import DjangoFilterBackend
from .fillters import productFillter

'''
 Functions API

@api_view('GET')
def product_list(request):
    queryset = product.objects.all()
    data = ProductSerializer(queryset, many=True).data
    return Response({'all_product':data})


@api_view('POST')
def edit_product(request):
    queryset = product.objects.all()
'''
# -------------------------------------------------------
    # Generics class API

class ProductListAPI(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = myPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price']
    filterset_class = productFillter
    search_fields = ['name']
    # permission_classes = [IsAuthenticated]


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = product
    permission_classes = [IsAuthenticated]
    serializer_class = productDetailSerializer  


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPI(generics.RetrieveAPIView):
    queryset = Category
    serializer_class = CategoryDetailSerializer


class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = CategorySerializer

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand
    serializer_class = BrandDetailSerializer



class ProductReviewsList(generics.ListAPIView):
    queryset = productReviews.objects.all()
    serializer_class = productReviewsSerializer
    permission_classes = [IsAuthenticated]



# Viewsets API
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = product.objects.all()