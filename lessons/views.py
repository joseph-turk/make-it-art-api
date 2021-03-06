from lessons.models import Lesson, Tag
from lessons.serializers import LessonSerializer, TagSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Public Views

class LessonList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonSingle(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Admin Views

class AdminLessonList(generics.ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AdminLessonSingle(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AdminTagList(generics.ListCreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AdminTagSingle(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
