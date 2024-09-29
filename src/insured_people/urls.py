from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("list/", views.insured_people_list, name="insured_people_list"),
    path("add/", views.add_insured_person, name="add_insured_person"),
    path("search/", views.search_insured_person, name="search_insured_person"),
    path("<int:pk>/detail/", views.insured_person_detail, name="insured_person_detail"),
    path("<int:pk>/edit/", views.edit_insured_person, name="edit_insured_person"),
    path("<int:pk>/delete/", views.delete_insured_person, name="delete_insured_person"),
]
