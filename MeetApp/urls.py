from django.urls import include, path
from rest_framework import routers
from .views import ProfileViewSet, EventViewSet, PREViewSet, UserView, UserViewSet

router = routers.DefaultRouter()
router.register(r'Profile', ProfileViewSet)
router.register(r'PRE', PREViewSet)
router.register(r'Event', EventViewSet)
router.register(r'users', UserViewSet)
router.register(r'Login', UserView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]