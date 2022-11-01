from rest_framework import serializers
from .models import product, Category, Brand, productReviews





class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    # category = CategorySerializer()
    # brand = BrandSerializer()

    price_with_tax = serializers.SerializerMethodField(method_name='price_with_tax')

    def price_with_tax(self, product):
        return product.price*1.1

    class Meta:
        model = product
        fields = '__all__'
        # fields = ['id', 'name',  'flag', 'brand', 'category', 'price_with_tax']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    Category_Products = ProductSerializer(source='product_category', many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'image','Category_Products']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



class BrandDetailSerializer(serializers.ModelSerializer):
    Brand_Products = ProductSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = ['id', 'name', 'image', 'Brand_Products']


class productReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = productReviews
        fields = '__all__'



class productDetailSerializer(serializers.ModelSerializer):
    reviews = productReviewsSerializer(source='product_review', many=True)
    class Meta:
        model = product
        fields = ['id', 'name', 'image', 'price', 'subtitle', 'flag', 'desc','brand' , 'category', 'video_url','quantity', 'reviews'] 