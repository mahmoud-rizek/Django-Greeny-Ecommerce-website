from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from .models import product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets

 # Functions API
@api_view(['GET'])
def product_list_api(request):
    objectList = product.objects.all()[:200]
    data = ProductSerializer(objectList, many=True).data
    return Response({'all_product':data})
 
@api_view(['GET'])
def product_detail_api(request, id):
    objectList = product.objects.get(id=id)
    data = ProductSerializer(objectList).data
    return Response({'product_detail':data})


# Generics class API
# class ProductListAPI(generics.ListCreateAPIView):
class ProductListAPI(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPI(generics.RetrieveAPIView ):
    queryset = product
    serializer_class = ProductSerializer



# Viewsets API
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProductSerializer
    queryset = product.objects.all()