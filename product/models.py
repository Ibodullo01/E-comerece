from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from parler.models import TranslatableModel, TranslatedFields

from .choise import CategoryType
from django.core.validators import MinValueValidator, MaxValueValidator
User = get_user_model()

from base.models import TimeStampedModel

class Category(TranslatableModel ,models.Model):
    translations = TranslatedFields(name = models.CharField(max_length=100 , unique=True))
    order = models.IntegerField(default=0)
    type = models.IntegerField(choices=CategoryType , default=CategoryType.NON_TYPE)

    def __str__(self):
        return self.name

class Product(TranslatableModel ,TimeStampedModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100),
        description = models.TextField(),
        details = models.JSONField(default=dict)
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True , related_name='products')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()


    # title = models.CharField(max_length=100)
    # description = models.TextField()
    # details = models.JSONField(default=dict)


    def __str__(self):
        return self.title6

    def save(self, *args, **kwargs):
        self.validate_detail()
        super().save(*args, **kwargs)

    def validate_detail(self):
        category_type = self.category.type
        if category_type ==1:
            required_keys = {'size' , 'color'}
        else:
            required_keys = set()

        missing_keys = required_keys - self.details.keys()
        if missing_keys:
            raise ValidationError(
                "Missing required keys for category type '%(category_type)s': %(missing_keys)s",
                params={'category_type': category_type, 'missing_keys': ', '.join(missing_keys)},
            )
class Image(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

class Comment(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=300)
    star = models.IntegerField(default=0 ,
                               validators=[MinValueValidator(0), MaxValueValidator(5)])


    def __str__(self):
        return self.text






