from rest_framework import serializers

from main.models import Product, Alert


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'stock',
            'expires_at'
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'stock',
            'expires_at',
            'created_at',
            'updated_at'
        )


class AlertListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = (
            'id',
            'product',
            'days_before',
            'alert_at',
            'active',
            'expired',
            'days_until_activation',
            'days_since_activation',
            'created_at',
            'updated_at'
        )
