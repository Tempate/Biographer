from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    url = models.URLField()
    desc = models.TextField()

    SEXES = [(0, "Male"), (1, "Female")]
    sex = models.IntegerField(choices=SEXES, default=0)

    DIFFICULTIES = [(1, "Easy"), (2, "Medium"), (3, "Hard")]
    difficulty = models.IntegerField(choices=DIFFICULTIES, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    people = models.ManyToManyField(Person)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
