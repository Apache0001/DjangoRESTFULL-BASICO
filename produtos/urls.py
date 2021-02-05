from django.urls import path

from .views import ProdutosAPIView

urlpatterns = [
    path('produtos/', ProdutosAPIView.as_view(), name="produtos")
]