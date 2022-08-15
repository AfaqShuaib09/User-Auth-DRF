from rest_framework.routers import DefaultRouter
from userApp.views import UserViewSet, ProfileViewSet, CreateProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'profile/create', CreateProfileViewSet, basename='create-profiles')

urlpatterns = router.urls 