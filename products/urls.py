from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandtDetail, CategoryList, testing_page
from .api import product_list_api, product_detail_api, ProductListAPI, ProductDetailAPI, UserViewSet

app_name = 'products'

urlpatterns = [

    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_details'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<int:pk>', BrandtDetail.as_view(), name='brand_details'),
    path('categorys/', CategoryList.as_view(), name='category_list'),
    path('testing/', testing_page),

    # API
    path("api/", product_list_api),
    path("api/<int:id>", product_detail_api),

    path("api/vs", UserViewSet.as_view({'get':'list'})),
    path("api/cbv", ProductListAPI.as_view()),
    path("api/cbv/<int:pk>", ProductDetailAPI.as_view()),


]
