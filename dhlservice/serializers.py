from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)
    countryCode = serializers.CharField(max_length=2)
    postalCode = serializers.CharField(max_length=10)

class PackageSerializer(serializers.Serializer):
    weight = serializers.FloatField()
    length = serializers.FloatField()
    width = serializers.FloatField()
    height = serializers.FloatField()

class ShipmentSerializer(serializers.Serializer):
    consignee = AddressSerializer()
    shipper = AddressSerializer()
    packages = PackageSerializer(many=True)

class TrackingSerializer(serializers.Serializer):
    tracking_number = serializers.CharField()
