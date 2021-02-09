import pytz
from django.db import models


class ActivityPeriod(models.Model):
    """Activity Period model."""

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        """Meta."""

        managed = True
        ordering = ["pk"]

    def __str__(self):
        """__str__."""
        return self.id


class User(models.Model):
    """User model."""
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    id = models.CharField(max_length=200, primary_key=True)
    real_name = models.CharField(max_length=500, null=True, blank=True)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    activity_map = models.ManyToManyField(ActivityPeriod)

    class Meta:
        """Meta."""

        managed = True
        ordering = ["pk"]

    def __str__(self):
        """__str__."""
        return self.real_name
