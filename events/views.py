from datetime import date
from events.models import Event, Registration
from events.serializers import EventSerializer, RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Public Event Views

class EventList(generics.ListAPIView):
    queryset = Event.objects.all().exclude(date__lt=date.today()).order_by('date')
    serializer_class = EventSerializer


class EventSingle(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Admin Event Views

class AdminEventList(generics.ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all().exclude(date__lt=date.today()).order_by('date')
    serializer_class = EventSerializer


class AdminEventListPast(generics.ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all().exclude(date__gt=date.today()).order_by('date')
    serializer_class = EventSerializer


class AdminEventSingle(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
