# encoding=utf-8

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'DANGEROUS! Clear all django-tables after initial migrations to make loaddata work'

    def handle(self, *args, **options):
        clear_django_tables()


def clear_django_tables():
    was_error = False

    from django.contrib.auth.models import Permission
    try:
        Permission.objects.all().delete()
        print("Permission cleared")
    except OperationalError:
        print("No Permission table present")
        was_error = True

    from django.contrib.contenttypes.models import ContentType
    try:
        ContentType.objects.all().delete()
        print("ContentType cleared")
    except OperationalError:
        print("No ContentType table present")
        was_error = True

    if was_error:
        print("Probably, you need to call ./manage.py migrate first")
