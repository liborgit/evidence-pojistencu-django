from django.contrib import admin
from django.urls import path, include
from insured_people import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_page, name="home_page"),
    path("insured_people/", include("insured_people.urls")),
]
