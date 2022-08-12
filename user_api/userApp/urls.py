from rest_framework.routers import DefaultRouter
from userApp.views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'profiles', ProfileViewSet, basename='profiles')

print(router.urls)
urlpatterns = router.urls 