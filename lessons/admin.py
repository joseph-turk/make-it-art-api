from django.contrib import admin

from lessons.models import Lesson, Material, Rubric, Resource, Tag

admin.site.register(Lesson)
admin.site.register(Material)
admin.site.register(Rubric)
admin.site.register(Resource)
admin.site.register(Tag)
