from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Content(models.Model):
    field_name = models.CharField(max_length=100)
    field_location = models.ForeignKey(
        Location, related_name='location', on_delete=models.CASCADE)
    field_content = models.TextField()

    def __str__(self):
        return self.field_name
