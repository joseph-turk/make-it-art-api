from rest_framework import serializers
from lessons.models import Lesson, Material, Resource, Rubric, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        partial = True


class LessonSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Lesson
        fields = '__all__'
        partial = True

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        lesson = Lesson.objects.create(**validated_data)
        for tag in tags_data:
            tag_object = Tag.objects.get(name=tag['name'])
            lesson.tags.add(tag_object)
        return lesson

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        instance = super(LessonSerializer, self).update(
            instance, validated_data)

        instance.tags.clear()

        for tag in tags_data:
            tag_object = Tag.objects.get(name=tag['name'])
            instance.tags.add(tag_object)

        return instance
