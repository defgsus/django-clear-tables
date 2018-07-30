# encoding=utf-8

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'DANGEROUS! Clear all django-tables after initial migrations to make loaddata work'

    def handle(self, *args, **options):
        clear_django_tables()



def clear_django_tables():
    from django.contrib.auth.models import Permission
    Permission.objects.all().delete()

    from django.contrib.contenttypes.models import ContentType
    ContentType.objects.all().delete()
