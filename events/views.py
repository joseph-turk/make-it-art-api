from datetime import date
from events.models import Event, Registration
from events.serializers import EventSerializer, RegistrationSerializer, RegistrationCreateSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Public Event Views

class EventList(generics.ListAPIView):
    queryset = Event.objects.all().exclude(date__lt=date.today()).order_by('date')
    serializer_class = EventSerializer


class EventSingle(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Public Registration Views

class RegistrationSingle(generics.RetrieveAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


@api_view(['POST'])
def create_registration(request):
    if request.method == 'POST':
        event_id = request.data['event']['id']
        registration = request.data
        event = Event.objects.get(pk=event_id)

        # Clean up request data
        registration.pop('event', None)
        registration['event'] = event_id

        # Check if event is full
        registration['is_wait_list'] = False
        if event.is_full:
            registration['is_wait_list'] = True

        is_full = False
        if len(event.registrations.all()) >= event.capacity - 1:
            is_full = True

        serializer = RegistrationCreateSerializer(data=registration)

        if serializer.is_valid():
            serializer.save()

            if is_full:
                event.is_full = True
                event.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


# Admin Registration Views

class AdminRegistrationSingle(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
