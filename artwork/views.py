from django.http import HttpResponse
from artwork.models import Artwork
from artwork.serializers import ArtworkSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Public Views

class ArtworkList(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class ArtworkSingle(generics.RetrieveAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


# Admin Views

class AdminArtworkList(generics.ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class AdminArtworkSingle(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
