from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Category


def home(request):
    people = ", ".join([person.name for person in Person.objects.all()])

    return render(request, "main/home.html", {"people": people})


def biography(request, name):
    context = {}

    context["person"] = get_object_or_404(Person, name=name)
    context["person"].desc = context["person"].desc.splitlines()

    return render(request, "main/biography.html", context)


def search(request):
    if request.method != "POST":
        return redirect("home")

    return redirect("biography", request.POST.get("name"))


def index(request, category=None):
    context = {}

    if not category:
        context["people"] = Person.objects.order_by('name')
        context["categories"] = Category.objects.order_by('name')
    else:
        _category = get_object_or_404(Category, name=category)
        context["people"] = _category.people.all()
        context["category"] = _category


    return render(request, "main/index.html", context)
