from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandtDetail, CategoryList, testing_page
from .api import  ProductListAPI, ProductDetailAPI, ProductReviewsList, CategoryListAPI, CategoryDetailAPI, BrandListAPI, BrandDetailAPI, UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'products'

urlpatterns = [

    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_details'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<int:pk>', BrandtDetail.as_view(), name='brand_details'),
    path('categorys/', CategoryList.as_view(), name='category_list'),
    path('testing/', testing_page),

 
    # Token

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API


    path("api/", ProductListAPI.as_view()),
    path("api/reviews", ProductReviewsList.as_view()),
    path("api/<int:pk>", ProductDetailAPI.as_view()),

    path("api/categorys", CategoryListAPI.as_view()),
    path("api/category/<int:pk>", CategoryDetailAPI.as_view()),


    path("api/brands", BrandListAPI.as_view()),
    path("api/brand/<int:pk>", BrandDetailAPI.as_view()),


    # API (ViewSets)

    path("api/vs", UserViewSet.as_view({'get':'list'})),
]
