''' urls definition for userApp '''
from rest_framework.routers import DefaultRouter

from userApp.views import ProfileViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'profiles', ProfileViewSet, basename='profiles')

urlpatterns = router.urls 
