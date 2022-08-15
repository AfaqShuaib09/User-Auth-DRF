from django.contrib.auth.models import User
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from userApp.models import Profile
from userApp.serializer import (ProfileSerializer, UpdateProfileSerializer,
                                UserSerializer)


# Create your views here.
class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """
    API endpoint that allows all users to be viewed or a single user by passing the id.\n
    GET -> list all users -> /api/users/ \n
    GET -> list a single user -> /api/users/id/
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'pk'


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed , created, updated or deleted.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'

    def create(self, request, *args, **kwargs):
        """
        Create a new profile associated with the user.
        """
        try:
            user = User.objects.get(username=request.data['username'])
            if Profile.objects.filter(user__username=user.username).exists():
                return Response({"message": "Profile already exists"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'User not found'}, status=404)
        user_profile = Profile.objects.create(user=user, 
                            full_name=request.data['full_name'],
                            cnic=request.data['cnic'],
                            contact_number=request.data['contact_number'],
                            address=request.data['address'],
                            gender = request.data['gender'],
                            country = request.data['country'])
        user_profile.save()
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        """
        Returns the serializer class for the viewset
        """
        return UpdateProfileSerializer if self.action == 'update' else self.serializer_class


# {
#         "username": "Faateh",
#         "profile": {
#             "full_name": "Faateh Sultan",
#             "cnic": "35202-2567834-3",
#             "contact_number": "+923064416400",
#             "address": "30 Huma Block",
#             "gender": "Male",
#             "country": "PK"
#         }
# }

# {
#     "user": {
#         "id" : 3,
#         "username" : "Faateh",
#         "email" : "faatehnigga@gmail.com"
#     }
#     "full_name": "Faateh Sultan",
#     "cnic": "35202-2567834-3",
#     "contact_number": "+923064416400",
#     "address": "30 Huma Block",
#     "gender": "Male",
#     "country": "PK"
# }