''' Serialization classes for the models used in the userApp application '''
from django.contrib.auth.models import User
from rest_framework import serializers, validators

from userApp.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializes the data to register/signup a user using POST request
    """
    class Meta:
        """
        Meta subclass to define fields.
        """
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True, 'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(queryset=User.objects.all(),
                    message='A user with same email already exists')
                    ]
                },
            }

    def create(self, validated_data):
        """
        Handles the validated data to create a user.
        """
        try:
            user = User.objects.create_user(
                validated_data['username'], validated_data['email'], validated_data['password']
            )
            return user
        except KeyError:
            raise (serializers.ValidationError("Required fields are missing 😔"))


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the data of a user.
    """
    class Meta:
        """
        Meta subclass to define fields.
        """
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ('id',)


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializes the data of a profile.
    """
    user = UserSerializer()

    class Meta:
        """
        Meta subclass to define fields.
        """
        model = Profile
        fields = ['user', 'full_name', 'cnic', 'contact_number', 'address', 'gender', 'country']
        read_only_fields = ('user',)
