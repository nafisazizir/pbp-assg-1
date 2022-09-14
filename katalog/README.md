# LINKS
[HOME](https://pbp-assg-2.herokuapp.com) -
[CATALOG](https://pbp-assg-2.herokuapp.com/katalog)

# DIAGRAM
![diagram_assg2 drawio](https://user-images.githubusercontent.com/101693218/189961793-8eed4504-2e98-4fbb-ad0c-5df9ed0e6e1c.png)

# WHY VIRTUAL ENVIROMENT?
There are various benefits of using virtual environment in Django:
- Virtual enviroment keeps the Python packages in a virtual environment localized to each project, instead of forcing to install the packages to the whole system
- Allows the user to have several virtual enviroment which means allow to have separate sets of packages for various projects, even though those different sets of packages would typically conflict with one another. For instance, virtual environment can keep projects which use two different django version seperated, allowing the users to simultaneously meet both requirements.
- It will be much easier to have different dependent packages for each projects, allowing the users to fully customize their requirements.txt
### Can Django app run without virtual environment?
Of course! Virtual environnemt is tool to make user easier to have multiple projects with different dependencies. However, django still can be run without virtual environment

# HOW TO IMPLEMENT?
1. In the first step I made `show_catalog()` function to query from `.json` data. The data is collected by using `CatalogItem.objects.all()` and assigned into variable `data_item_catalog`. Then, render into HTML using `render()`
2. Secondly, I made the routing to map the function that I've made in `1.`. I add the url path in `/katalog/urls.py` with `path('', show_catalog, name='show_catalog')` and in `/project_django/urls.py` add `path('katalog/', include('katalog.urls'))`
3. Then, I map the data that has been rendered into HTML by iterating the data and present into nice table. In `/katalog/template/katalog.html` add:
```
    {% comment %} Add the data below this line {% endcomment %}
    {% for barang in list_barang %}
    <tr>
        <th>{{barang.item_name}}</th>
        <th>{{barang.item_price}}</th>
        <th>{{barang.item_stock}}</th>
        <th>{{barang.description}}</th>
        <th>{{barang.rating}}</th>
        <th>{{barang.item_url}}</th>
    </tr>
    {% endfor %}
```
4. To run the app in local (and check if the app already correct), I did this following command( run seperately for each line):
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_catalog_data.json
```
5. After that, I run the django project by `python manage.py runserver` and the app can be open in http://localhost:8000/ for HOME or http://localhost:8000/katalog for KATALOG
6. To deploy the app, I add, commit and push the local repository to the github. Make new app in Heroku, enter the repository secret in github, and re-run the job. It's done!
