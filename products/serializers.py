from rest_framework import serializers
from .models import product, Category, Brand, productReviews







class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


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


class productReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = productReviews
        fields = '__all__'