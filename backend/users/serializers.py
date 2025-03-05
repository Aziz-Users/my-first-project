from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework.authtoken.models import Token


class UserProfileSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(source='profile.image', allow_null=True, required=False)
    balance = serializers.DecimalField(source='profile.balance', max_digits=10, decimal_places=2, required=False,read_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'image', 'balance', 'id']
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        image = profile_data.get('image')

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()


        if image:
            instance.profile.image = image
            instance.profile.save()

        return instance
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {
            'username': {
                'required': True,
                'error_messages': {
                    'required': 'Это поле обязательно для заполнения.',
                    'blank': 'Имя пользователя не может быть пустым.'
                }
            },
            'password': {
                'required': True,
                'write_only': True,
                'min_length': 8,
                'error_messages': {
                    'required': 'Это поле обязательно для заполнения.',
                    'blank': 'Пароль не может быть пустым.',
                    'min_length': 'Пароль должен содержать как минимум 8 символов.'
                }
            },
            'email': {
                'required': True,
                'error_messages': {
                    'required': 'Это поле обязательно для заполнения.',
                    'blank': 'Email не может быть пустым.',
                    'invalid': 'Введите корректный адрес электронной почты.'
                }
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user