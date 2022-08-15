import profile
import pdb 
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from userApp.serializer import UserSerializer, ProfileSerializer, CreateProfileSerializer
from userApp.models import Profile

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


class CreateProfileViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    API endpoint that allows users to be viewed , created, updated or deleted.
    """
    pdb.set_trace()
    queryset = Profile.objects.all()
    serializer_class = CreateProfileSerializer

    def get_serializer_class(self):
        return CreateProfileSerializer if self.request.method == 'POST' else ProfileSerializer
