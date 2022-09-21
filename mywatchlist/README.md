# LINKS
[HOME](https://pbp-assg-2.herokuapp.com) -
[MY WATCHLIST HTML](https://pbp-assg-2.herokuapp.com/mywatchlist/html/) -
[MY WATCHLIST XML](https://pbp-assg-2.herokuapp.com/mywatchlist/xml/) -
[MY WATCHLIST JSON](https://pbp-assg-2.herokuapp.com/mywatchlist/json/) -

## JSON, XML and HTML
HTML (Hyper Text Markup Language) and XML (Extensible Matkup Language) has some differences. XML more focus on what the data is about, and describing the data. While HTML is more focus on how the data looks like and displaying the data. Tag type in XML is user defined, but in HTML is predefined. HTML extension file can be .html or .htm, and XML file extension is .xml. JSON (JavaScript Object Notation)'s file are easier to read than XML file. Different with XML, JSON doesn't have end tags. Nowadays, JSON are more popular and better than XML due to several reasons. XML is much more difficult to parse than JSON, and also JSON is parsed into a ready-to-use JavaScript object. 

## Why we need data delivery when implementing on a platform?
Data delivery is such an important part when implementing on a platform, since it allows the computer to interract with the users by delivering the data. So, data delivery can make the process easier when making a platform.

## How to implement?
1. Create new app `mywatchlist` by using this command
```python manage.py startapp mywatchlist```
2. Add mywatchlist URL path by appending `mywatchlist` in the `project_django/settings.py` and add `path('mywatchlist/', include('mywatchlist.urls'))` in `project_django/urls.py`
3. Create model in `mywatchlist/models.py` by using this funtion:
```shell
    class MyWatchListItem(models.Model):
    watched = models.CharField(max_length=255)
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
```
4. Create 10 data entries in `mywatchlist/fixtures/initial_mywatchlist_data.json`
5. Implementing a feature to show the data in `mywatchlist/views.py`
```shell
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
```
6. Add the url pattern in `mywatchlist/urls.py`
```shell
from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json
from mywatchlist.views import show_html

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
] 
```
7. Then, deploy the app in the HEROKU by pull, add, commit, and push to GitHub