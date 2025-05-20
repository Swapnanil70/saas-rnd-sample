from django.http import HttpResponse
from django.shortcuts import render
import pathlib

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = "Home Page"
    my_context = {"title": my_title}
    html_template = "home.html"

    PageVisit.objects.create(path=request.path)

    return render(request, html_template, my_context)