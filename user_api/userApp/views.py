""" Viewsets declaration for the userApp application """
import re

from django.contrib.auth.models import User
from knox.models import AuthToken
from rest_framework import mixins, status, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from userApp.models import Profile
from userApp.permissions import IsOwnerOrReadOnly
from userApp.serializer import (ProfileSerializer, RegisterSerializer, UserSerializer)
from userApp.utils import validate_cnic, validate_contact_number, validate_gender

# Create your views here.
class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    This view provides a post request to register a user.
    """
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        """
        Handles the request to register/create a user.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })


class LoginViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    This view provides a post request to login a user.
    """
    serializer_class = AuthTokenSerializer
    permission_classes = (AllowAny,)

    def create(self, request):
        """
        Handles the request to login a user.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = AuthToken.objects.create(user)[1]
        return Response({'token': token})


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    """
    API endpoint that allows all users to be viewed or a single user by passing the id.\n
    GET -> list all users -> /api/users/ \n
    GET -> list a single user -> /api/users/id/
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed, created, updated or deleted.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

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

        if request.user != User.objects.get(username=request.data['username']):
            return Response({"message": "Creation of other user profile not allowed"})

        if request.data.get('cnic'):
            if not validate_cnic(request.data.get('cnic')):
                return  Response({'message': 'Invalid CNIC Format xxxxx-xxxxxx-x'},
                                        status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('contact_number'):
            if not validate_contact_number(request.data.get('contact_number')):
                return Response({'message': 'Invalid Contact No. (Format +XXXXXXXXXXXX)'},
                                    status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('gender'):
            if not validate_gender(request.data.get('gender')):
                return Response({'message': 'not a valid choice for gender'},
                                    status=status.HTTP_400_BAD_REQUEST)

        user_profile = Profile.objects.create(user=user,
                            full_name=request.data.get('full_name', ''),
                            cnic=request.data.get('cnic', ''),
                            contact_number=request.data.get('contact_number', ''),
                            address=request.data.get('address', ''),
                            gender = request.data.get('gender', 'Do not specify'),
                            country = request.data.get('country', 'PK'),
                        )
        user_profile.save()
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, *args, **kwargs):
        """
        Update an existing profile associated with the user.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = ProfileSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
