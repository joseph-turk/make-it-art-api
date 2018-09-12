from django.db import models
from datetime import date


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    capacity = models.IntegerField()
    graphic = models.ImageField(upload_to='events')
    is_full = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def is_past(self):
        return self.date < date.today()

    @property
    def num_registered(self):
        num = 0

        for registration in self.registration_set.all():
            if not registration.is_wait_list:
                num += 1

        return num

    @property
    def num_wait_list(self):
        num = 0

        for registration in self.registration_set.all():
            if registration.is_wait_list:
                num += 1

        return num


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    is_wait_list = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} (Registered for {self.event.name})'
