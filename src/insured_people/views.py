import unicodedata
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.cache import never_cache
from .forms import InsuredPersonForm
from .models import InsuredPerson

def home_page(request):
    return render(request, "homepage.html")

@never_cache
def insured_people_list(request):
    insured_people = InsuredPerson.objects.all()
    return render(request, "list.html", {"insured_people": insured_people})

def remove_diacritics(input_str):
    normalized = unicodedata.normalize("NFKD", input_str)
    return "".join([c for c in normalized if not unicodedata.combining(c)])

def search_insured_person(request):
    query = request.GET.get("q", "").strip()
    insured_people = []

    if query:
        normalized_query = remove_diacritics(query.lower())
        split_query = normalized_query.split()

        all_people = InsuredPerson.objects.all()

        for person in all_people:
            first_name = remove_diacritics(person.first_name.lower())
            last_name = remove_diacritics(person.last_name.lower())

            if len(split_query) == 2:
                if (split_query[0] in first_name and split_query[1] in last_name) or \
                        (split_query[0] in last_name and split_query[1] in first_name):
                    insured_people.append(person)

            elif len(split_query) == 1:
                if split_query[0] in first_name or split_query[0] in last_name:
                    insured_people.append(person)

    return render(request, "search.html", {"insured_people": insured_people, "query": query})

@never_cache
def add_insured_person(request):
    if request.method == "POST":
        form = InsuredPersonForm(request.POST)
        if form.is_valid():
            insured_person = form.save()
            messages.success(request, "Pojištěnec byl úspěšně přidán.")
            return redirect(reverse("insured_person_detail", kwargs={"pk": insured_person.pk}))
    else:
        form = InsuredPersonForm()

    return render(request, "add.html", {"form": form})

@never_cache
def insured_person_detail(request, pk):
    insured_person = get_object_or_404(InsuredPerson, pk=pk)
    return render(request, "detail.html", {"insured_person": insured_person})

@never_cache
def edit_insured_person(request, pk):
    insured_person = get_object_or_404(InsuredPerson, pk=pk)
    if request.method == "POST":
        form = InsuredPersonForm(request.POST, instance=insured_person)
        if form.is_valid():
            form.save()
            messages.success(request, "Změny byly úspěšně uloženy.")
            return redirect(reverse("edit_insured_person", kwargs={"pk": insured_person.pk}))
    else:
        form = InsuredPersonForm(instance=insured_person)

    return render(request, "edit.html", {"form": form, "insured_person": insured_person})

@never_cache
def delete_insured_person(request, pk):
    insured_person = get_object_or_404(InsuredPerson, pk=pk)
    if request.method == "POST":
        insured_person.delete()
        messages.success(request, "Pojištěnec byl úspěšně smazán.")
        return redirect("add_insured_person")
