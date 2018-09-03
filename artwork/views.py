from django.http import HttpResponse
from artwork.models import Artwork
from artwork.serializers import ArtworkSerializer
from rest_framework import generics


def index(request):
    return HttpResponse('Hello, world! This is the artwork index.')


class ArtworkList(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class ArtworkSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
