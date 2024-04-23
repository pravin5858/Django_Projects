from rest_framework import serializers
from .models import Brand, Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer
    class Meta:
        model = Product
        fields = "__all__"