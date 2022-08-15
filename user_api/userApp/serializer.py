from django.contrib.auth.models import User
from rest_framework import serializers
from userApp.models import Profile
import pdb

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
    class Meta:
        """
        Meta subclass to define fields.
        """
        model = Profile
        fields = ['user','full_name', 'cnic', 'contact_number', 'address', 'gender', 'country']
        read_only_fields = ('user',)
    

class CreateProfileSerializer(serializers.Serializer):
    # add username custom field
    username = serializers.CharField()
    profile = ProfileSerializer()

    class Meta:
        fields = (
            'username',
            'profile'
        )

    def create(self, validated_data):
        import pdb; pdb.set_trace()
        tmp_profile = validated_data.pop('profile')
        user = User.objects.get(username=validated_data['username'])
        profile = Profile.objects.create(
            user=user,
            full_name=tmp_profile['full_name'],
            cnic=tmp_profile['cnic'],
            contact_number=tmp_profile['contact_number'],
            address=tmp_profile['address'],
            gender = tmp_profile['gender'],
            country = tmp_profile['country']
        )
        return profile
