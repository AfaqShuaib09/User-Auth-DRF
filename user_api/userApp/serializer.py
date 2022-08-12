from django.contrib.auth.models import User
from rest_framework import serializers
from userApp.models import Profile

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
