from django.shortcuts import render
from .models import App


def home(request):
    apps = App.objects.all()
    return render(request, template_name="index.html", context={"apps": apps})
