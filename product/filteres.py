import django_filters

from product.models import Product


class ProductFilter(django_filters.FilterSet):
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['price_gte', 'price_lte']

