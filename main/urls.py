from django.urls import path

from main import views

urlpatterns = [
    path('products/', views.ProductCreateAPIView.as_view(), name='products'),
    path('products/<int:id>/', views.ProductRetrieveAPIView.as_view(), name='product'),
    path('products/<int:id>/alerts', views.ProductAlertsAPIView.as_view(), name='product_alerts'),
]