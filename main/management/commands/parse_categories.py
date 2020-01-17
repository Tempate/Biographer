from django.core.management.base import BaseCommand, CommandError
from main.categories import remove_trivial_categories, merge_categories
from main.models import Category

class Command(BaseCommand):
    help = 'Parses categories to make them more general.'

    def handle(self, *args, **options):
        initial_cats = len(Category.objects.all())

        clean_categories()

        resulting_cats = len(Category.objects.all())

        self.stdout.write(self.style.SUCCESS('Successfully removed %d categories out of %d.' % (
            initial_cats - resulting_cats,
            resulting_cats
        )))
