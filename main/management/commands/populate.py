from django.core.management.base import BaseCommand, CommandError
from main.models import Person
from main.helpers import add_person
from main.categories import clean_categories

class Command(BaseCommand):
    help = 'Adds entries to the database. It expects a file with a list of'\
            'names with their own wikipedia page, one per line.'

    def add_arguments(self, parser):
        parser.add_argument("filename", nargs=1, type=str)

    def handle(self, *args, **options):
        filename = options["filename"][0]

        try:
            file = open(filename, "r")
            people = file.read().splitlines()
            file.close()
        except FileNotFoundError:
            raise CommandError("File '%s' not found" % filename)

        count = 0

        for person in people:
            if add_person(person):
                count += 1

        clean_categories()

        self.stdout.write(self.style.SUCCESS('Successfully added %d people out of %d' % (count, len(people))))
