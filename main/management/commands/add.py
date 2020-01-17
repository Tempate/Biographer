from django.core.management.base import BaseCommand, CommandError
from main.models import Person
from main.helpers import add_person

class Command(BaseCommand):
    help = 'Adds a person to the database.'

    def add_arguments(self, parser):
        parser.add_argument("name", nargs=1, type=str)

    def handle(self, *args, **options):
        person = options["name"][0]

        if add_person(person):
            self.stdout.write(self.style.SUCCESS('%s was successfully added' % person))
        else:
            self.stdout.write(self.style.ERROR('There was an error adding %s' % person))
