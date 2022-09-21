from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist_item = MyWatchListItem.objects.all()
    not_yet = 0
    watched = 0
    mess = ""
    for movies in data_watchlist_item:
        if movies.watched:
            watched +=1
        else:
            not_yet += 1
    if watched >= not_yet:
        mess = "Congratulations, you have watched a lot of movies!"
    else:
        mess  = "Woah, you need to watch more movies!"
    context = {
        'list_item': data_watchlist_item,
        'name' : 'Nafis Azizi Riza',
        'npm' : 2106658843,
        'mess' : mess
    }
    return render(request, "mywatchlist.html", context)

def show_html(request):
    data_watchlist_item = MyWatchListItem.objects.all()
    not_yet = 0
    watched = 0
    mess = ""
    for movies in data_watchlist_item:
        if movies.watched:
            watched +=1
        else:
            not_yet += 1
    if watched >= not_yet:
        mess = "Congratulations, you have watched a lot of movies!"
    else:
        mess  = "Woah, you need to watch more movies!"
    context = {
        'list_item': data_watchlist_item,
        'name' : 'Nafis Azizi Riza',
        'npm' : 2106658843,
        'mess' : mess
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")