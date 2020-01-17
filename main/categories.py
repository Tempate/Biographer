from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from .models import Category

from textblob import TextBlob
import re


def clean_categories():
    remove_trivial_categories()
    merge_categories()


def remove_trivial_categories():
    """ Removes categories that only have one element. """
    Category.objects\
        .annotate(people_count=Count('people'))\
        .filter(people_count=1)\
        .delete()


def merge_categories():
    """ Merges categories to other with their name in plural. """

    categories = Category.objects.all()

    for category in categories:
        try:
            _category = Category.objects.get(name=category.name+'s')

            for person in category.people.all():
                _category.people.add(person)

            category.delete()
        except ObjectDoesNotExist:
            pass


def link_categories(person, wiki_page):
    """ Links a person to the categories of their wikipedia page. """

    categories = extract_categories(wiki_page)

    for category in categories:
        _category = get_or_create_category(category.title())
        _category.people.add(person)


def extract_categories(wiki_page):
    """ Extracts the categories from a wikipedia article. """

    category_re = re.compile(r'^Category:[0-9]+[a-z]+\-century( BC| BCE)? (?P<category>.+)$')

    wiki_categories = set()

    for category in wiki_page.categories.keys():
        match = category_re.match(category)

        if match:
            wiki_categories.add(match.group("category"))

    categories = set()

    for name in wiki_categories:
        for (category, pos) in TextBlob(name).pos_tags:
            if pos[0] == 'N':
                categories.add(category)

    return categories


def get_or_create_category(name):
    """ Tries to find a category with the given name or with name + 's',
    creates a new one if it can't find it. """

    if Category.objects.filter(name=name).exists():
        return Category.objects.get(name=name)

    if Category.objects.filter(name=name + 's').exists():
        return Category.objects.get(name=name + 's')

    category = Category(name=name)
    category.save()

    return category
