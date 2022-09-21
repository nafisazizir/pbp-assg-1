from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist_item = MyWatchListItem.objects.all()
    context = {
        'list_item': data_watchlist_item,
        'name' : 'Nafis Azizi Riza',
        'npm' : 2106658843
    }
    return render(request, "mywatchlist.html", context)

def show_html(request):
    data_watchlist_item = MyWatchListItem.objects.all()
    context = {
        'list_item': data_watchlist_item,
        'name' : 'Nafis Azizi Riza',
        'npm' : 2106658843
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")