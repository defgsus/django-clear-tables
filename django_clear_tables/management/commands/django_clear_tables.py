# encoding=utf-8
import sys

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
        sys.stdout.write("Permission cleared\n")
    except OperationalError:
        sys.stderr.write("No Permission table present\n")
        was_error = True

    from django.contrib.contenttypes.models import ContentType
    try:
        ContentType.objects.all().delete()
        sys.stdout.write("ContentType cleared\n")
    except OperationalError:
        sys.stderr.write("No ContentType table present\n")
        was_error = True

    if was_error:
        sys.stderr.write("Probably, you need to call './manage.py migrate' first\n")
