import random
import string
from datetime import timedelta

import names
import pytz
from django.core.management.base import BaseCommand
from randomtimestamp import randomtimestamp
from django.db import transaction

from activity_app.models import User, ActivityPeriod


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Command(BaseCommand):
    help = 'populate the dummy database.'

    @transaction.atomic
    def handle(self, *args, **options):
        for _ in range(10):
            user_obj = User.objects.create(id=id_generator(), real_name=names.get_full_name(),
                                           tz=random.choice(TIMEZONES)[0])

            for _ in range(5):
                start_time = randomtimestamp(start_year=2021, text=False)
                end_time = start_time + timedelta(hours=1)
                actvity_obj = ActivityPeriod.objects.create(start_time=start_time, end_time=end_time)
                user_obj.activity_map.add(actvity_obj)
                user_obj.save()
