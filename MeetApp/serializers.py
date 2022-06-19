from .models import Event, Profile, Profile_Event_Relation
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['Event_ID', 'title',
                  'city', 'address','date','description','x','y']
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['Profile_ID','user',
                  'name','email',
                  'description', 'profile_image','created']
class PERSerializer(serializers.HyperlinkedModelSerializer): #Profile_Event_Relation
    class Meta:
        model = Profile_Event_Relation
        fields = ['Profile_ID', 'Event_ID',
                  'Owner']
