''' urls definition for userApp '''
from django.urls import include, path
from knox import views as knox_views
from rest_framework.routers import DefaultRouter

from userApp.views import (LoginViewSet, ProfileViewSet, RegisterViewSet,
                           UserViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset'))
]
