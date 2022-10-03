from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandtDetail, CategoryList, testing_page
from .api import product_list_api

app_name = 'products'

urlpatterns = [

    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_details'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<int:pk>', BrandtDetail.as_view(), name='brand_details'),
    path('categorys/', CategoryList.as_view(), name='category_list'),
    path('testing/', testing_page),

    path("api/", product_list_api),
]
