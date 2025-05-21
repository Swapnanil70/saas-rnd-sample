from django.http import HttpResponse
from django.shortcuts import render
import pathlib

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    my_title = "Home Page"
    my_context = {"title": my_title,
                  "page_views": page_qs.count(),
                  "percent": 100 if qs.count() == 0 else round(page_qs.count() * 100 / qs.count(), 2),
                  "total_views": qs.count()}
    html_template = "home.html"

    PageVisit.objects.create(path=request.path)

    return render(request, html_template, my_context)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    my_title = "About Page"
    my_context = {"title": my_title,
                  "page_views": page_qs.count(),
                  "percent": 100 if qs.count() == 0 else round(page_qs.count() * 100 / qs.count(), 2),
                  "total_views": qs.count()}
    html_template = "home.html"

    PageVisit.objects.create(path=request.path)

    return render(request, html_template, my_context)