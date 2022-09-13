from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_item_catalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_item_catalog,
    'name': 'Nafis Azizi Riza',
    'npm' : '2106658843'
}
    return render(request, "katalog.html", context)