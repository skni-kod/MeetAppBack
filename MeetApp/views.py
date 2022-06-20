from .models import Profile, Profile_Event_Relation, Event
from rest_framework import viewsets
from .serializers import PERSerializer, ProfileSerializer, EventSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PREViewSet(viewsets.ModelViewSet):
    queryset = Profile_Event_Relation.objects.all()
    serializer_class = PERSerializer