from django.shortcuts import render
from django.http import HttpResponse
from .models import Repetitor

def index(request):
    items = Repetitor.objects.all()
    context = {
        'items': items,
    }
    return render(request, "myapp/index.html", context)


def indexItem(request, my_id):
    item = Repetitor.objects.get(id=my_id)
    context = {
        'item': item,
    }
    return render(request, "myapp/detail.html", context=context)
