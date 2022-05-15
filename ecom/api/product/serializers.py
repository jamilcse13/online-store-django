from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        image = serializers.ImageField(
            max_length=None, allow_empty_file=False, allow_null=True, required=False)
        
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category')