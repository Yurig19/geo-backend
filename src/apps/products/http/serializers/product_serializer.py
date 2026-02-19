from rest_framework import serializers


class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    unit_price = serializers.FloatField(min_value=0)
    quantity = serializers.IntegerField(min_value=0)


class ProductUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    unit_price = serializers.FloatField(min_value=0)


class StockOperationSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)


class ProductResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    unit_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )
    quantity = serializers.IntegerField(read_only=True)
    total_value = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True,
    )
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
