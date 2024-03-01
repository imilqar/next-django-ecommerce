from rest_framework import serializers

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecificationValue,
)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "alt_text", "is_feature"]


class SpecificationValueSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ProductSpecificationValue
        fields = ["name", "value"]

    def get_name(self, obj):
        return obj.specification.name if obj.specification.name else None


class ProductSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)
    product_specification_value = SpecificationValueSerializer(
        many=True, read_only=True
    )
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "category_name",
            "name",
            "desc",
            "slug",
            "price",
            "product_image",
            "product_specification_value",
        ]

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
