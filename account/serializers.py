from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework.validators import UniqueValidator
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(
                                       queryset=User.objects.all())])
    password = serializers.CharField(write_only=True,
                                     required=True,
                                     validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': False, 'allow_null': True},
            'last_name': {'required': False, 'allow_null': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
