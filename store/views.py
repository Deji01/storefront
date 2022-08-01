from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from requests import request
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from store.filters import ProductFilter
from store.permissions import IsAdminOrReadOnly
from .models import Cart, Collection, Customer, Order, OrderItem, Product, Review
from .serializers import AddCartItemSerializer, CartItemSerializer, CartSerializer, CollectionSerializer, CreateOrderSerializer, CustomerSerializer, OrderSerializer, ProductSerializer, ReviewSerializer, UpdateCartItemSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class CartViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return Cart.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_class = ProductFilter
    ordering_field = ['unit_price', 'last_update']
    search_fields = ['title', 'description']
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'})

        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']):
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'})

        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny]
        return [IsAuthenticated]

    @action(detail=False, methods = ['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data, context={'user_id': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        customer_id = Customer.objects.only('id').get(user_id = self.request.user.id)
        return  Order.objects.filter(customer_id=customer_id)
 

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer
        return super().get_serializer_class()


