from rest_framework import serializers
from lessons.models import Lesson, Material, Resource, Rubric, Tag


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        partial = True
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        partial = True
