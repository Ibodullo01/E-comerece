from django.core.cache import cache
from django.db.models import Prefetch, OuterRef, Subquery
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated
from .serilizers import CategorySerializer, ProductSerializer, ProductDetailSerializer, CommentSerializer
from product.models import Product , Category , Comment , Image

class CategoryListApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    # bu yerda get_queryset biz tushunib oldik
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     ids = [1 , 3]
    #     qs = qs.filter(id__in=ids)
    #     return qs




class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        products = cache.get('product_list')
        if products is None:
            # products = Product.objects.prefetch_related(
            #     Prefetch('image_set' , queryset=Image.objects.order_by('id'))
            # )
            main_image_subquery = Image.objects.filter(
                product=OuterRef('pk'),
            ).values('image')[:1]

            products = Product.objects.annotate(main_image=Subquery(main_image_subquery)
                    )

            cache.set('product_list' , products)
        # cache.delete('product_list')
        return products



class ProductByCategoryApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        qs = cache.get('product_by_category')
        # qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        qs = qs.filter(category__pk=pk)
        cache.set('product_by_category', qs)
        return qs

class ProductDetailApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CommentCreateApiView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated , )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentByProductApiView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        qs = qs.filter(product__pk=pk)
        return qs










