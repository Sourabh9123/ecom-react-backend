from rest_framework.serializers import ModelSerializer

from cartapp.models import Orderitem
from storeapp.models import Product
from storeapp.serializers import ProductSerializer



class OrderSerializers(ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Orderitem
        fields = ("product", "order", "created_at", "updated_at")

