import datetime

from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from rest_framework.views import Response
from rest_framework.exceptions import APIException
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from main.models import Alert, Product


@permission_classes([IsAuthenticated])
class ProductRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    from main.serializers import ProductDetailSerializer
    lookup_field = "id"
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


@permission_classes([IsAuthenticated])
class ProductCreateAPIView(generics.ListCreateAPIView):
    from main.serializers import ProductCreateSerializer
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        # Retrieve query parameters from the request
        order_by = self.request.query_params.get('order_by')
        expires_min = self.request.query_params.get('expires_min')
        expires_max = self.request.query_params.get('expires_max')

        queryset = Product.objects.all()
        date_format = '%Y-%m-%d'

        try:
            if order_by:
                queryset = queryset.order_by(order_by)

            if expires_min:
                queryset = queryset.filter(expires_at__gte=datetime.datetime.strptime(expires_min, date_format).date())

            if expires_max:
                queryset = queryset.filter(expires_at__lte=datetime.datetime.strptime(expires_max, date_format).date())
        except Exception as e:
            raise APIException(str(e))
        else:
            return queryset


@permission_classes([IsAuthenticated])
class ProductAlertsAPIView(generics.ListAPIView):
    from main.serializers import AlertListSerializer
    serializer_class = AlertListSerializer

    def get_queryset(self):
        product_id = self.kwargs.get("id")
        queryset = Alert.objects.filter(product_id=product_id)
        return queryset

    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get("id")
        # If product if doesnt' exist, return 404
        if not Product.objects.filter(id=product_id).exists():
            response_data = {'detail': 'No result found for Product with id ' + str(product_id) + '.'}
            return Response(response_data, status=404)
        return super().get(request, *args, **kwargs)