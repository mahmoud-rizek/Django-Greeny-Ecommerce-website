from .models import product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer




@api_view(['GET'])
def product_list_api(request):
    objects = product.objects.all()[:50]
    data = ProductSerializer(objects, many=True).data
    return Response({'status':200, 'all_product':data})



