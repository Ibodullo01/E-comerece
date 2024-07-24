from parler.models import TranslatedFields
from parler_rest.serializers import TranslatableModelSerializer
from rest_framework import serializers

from product.models import Product, Category, Image, Comment


class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFields(shared_model=Category)

    class Meta:
        model = Category
        fields = ['pk', 'translations', 'order']

    def to_representation(self, obj):
        data = super().to_representation(obj)
        # bu yerda get_FEILDNAME_display()  choise feild uchun ishlatiladi
        data['type_name'] = obj.get_type_display()
        return data


class ProductSerializer(serializers.ModelSerializer):

    main_image = serializers.CharField()

    class Meta:
        model = Product
        fields = ['pk', 'title', 'price', 'main_image']

    def get_main_image(self, obj):
        main_image = Image.objects.filter(product=obj).first()
        if main_image:
            return main_image.image.url
        return ''


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['pk', 'image']


class ProductDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['pk', 'title', 'description', 'price', 'category', 'images', 'details', 'quantity']

    def get_images(self, obj):
        images = Image.objects.filter(product=obj)
        serializer = ImageSerializer(images, many=True)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'text' , 'star'  , 'product']


