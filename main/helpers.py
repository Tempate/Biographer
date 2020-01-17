from .models import Person, Category
from .categories import link_categories
from .parsing import parse_description

import wikipediaapi
import re


def add_person(name):
    """ Adds a new person to the database.
    @input: The name of someone in wikipedia (e.g. John von Neumann).
    @output: The operation's success. """

    wiki = wikipediaapi.Wikipedia('en')

    try:
        wiki_page = wiki.page(name)
        person = Person(
                    name=name,
                    url=wiki_page.fullurl,
                    desc=parse_description(wiki_page.summary))
        person.save()

        link_categories(person, wiki_page)
    except Exception as e:
        print(name + ': ' + str(e))
        return False

    return True
