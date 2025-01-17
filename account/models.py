
from django.contrib.auth.models import AbstractUser
from django.db import models

from account.choices import UserType


class User(AbstractUser):
    user_type = models.IntegerField(choices=UserType, default=UserType.CUSTOMER)
    phone_number = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return self.username


    @property
    def is_admin(self):
        return self.user_type == 0

    @property
    def is_customer(self):
        return self.user_type == 1