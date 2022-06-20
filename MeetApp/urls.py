from django.urls import include, path
from rest_framework import routers
from .views import ProfileViewSet, EventViewSet, PREViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'Profile', ProfileViewSet)
router.register(r'PRE', PREViewSet)
router.register(r'Event', EventViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]