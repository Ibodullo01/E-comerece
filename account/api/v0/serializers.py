from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, date):
        password = date.get('password')
        password2 = date.pop('password2')
        if password != password2:
            raise serializers.ValidationError("password1 is not the same as password2")
        return date


    def create(self, data):
        user = User(
            username=data['username'],
            email=data['email'],
        )
        user.set_password(data['password'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone']

# class ChangeUserPasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         password = data.get('password')
#         if password != ]