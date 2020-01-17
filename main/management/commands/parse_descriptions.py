from django.core.management.base import BaseCommand, CommandError
from main.models import Person
from main.parsing import parse_description

class Command(BaseCommand):
    help = 'Parses descriptions to remove special marks.'

    def handle(self, *args, **options):
        people = Person.objects.all()

        for person in people:
            person.desc = parse_description(person.desc)
            person.save()

        self.stdout.write(self.style.SUCCESS('Successfully parsed %d descriptions' % len(people)))
