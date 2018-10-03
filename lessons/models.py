from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=1000)
    inspiration = models.TextField()
    outcomes = models.TextField()
    procedure = models.TextField()
    exit_expectations = models.TextField()
    finish_notes = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=1000, blank=True)
    file = models.FileField(null=True)
    attribution = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)
    lesson = models.ForeignKey(
        Lesson, related_name='resource_lesson', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=1000)
    lesson = models.ForeignKey(
        Lesson, related_name='material_lesson', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rubric(models.Model):
    name = models.CharField(max_length=1000)
    criteria = models.CharField(max_length=1000)
    lesson = models.ForeignKey(
        Lesson, related_name='rubric_lesson', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
