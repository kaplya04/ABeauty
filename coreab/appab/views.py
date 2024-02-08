# Create your views here.
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect


def index(request):
    if request.method == 'POST':
        form = BackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BackForm()
    data = {
        'form': form,
    }
    return render(request, "appab/index.html", data)


def about(request):
    return render(request, "appab/about.html")


def services(request):
    tovar = Tovar.objects.all()
    data = {
        'tovar': tovar,
    }
    return render(request, "appab/services.html", data)


def test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../services")
    else:
        form = TestForm()
    data = {
        "form": form,
    }
    return render(request, "appab/test.html", data)
