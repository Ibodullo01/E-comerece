from django.db import models

class CategoryType(models.IntegerChoices):
    NON_TYPE = 0 , 'None_type'
    CLOTHES = 1, 'Clothes'
    FOOD = 2, 'Food'
