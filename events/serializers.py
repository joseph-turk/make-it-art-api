from rest_framework import serializers
from .models import Event, Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        partial = True
        depth = 1


class RegistrationEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('id', 'name', 'email', 'is_wait_list')
        partial = True


class RegistrationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('name', 'email', 'is_wait_list', 'event')


class EventSerializer(serializers.ModelSerializer):
    registrations = RegistrationEventSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        partial = True
