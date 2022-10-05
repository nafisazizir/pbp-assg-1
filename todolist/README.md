# LINKS
[HOME](https://pbp-assg-2.herokuapp.com) -
[TODOLIST](https://pbp-assg-2.herokuapp.com/todolist/)

## What does `{% csrf_token %}` do in the `<form>` element? What happens if there is no such "code snippet" in the `<form>` element?
Cross-site request forgeries (CSRF) are a sort of malicious exploit in which unauthorized actions are taken on behalf of a user who has been authenticated. By comparing the token entered by the user with the one saved in the user session, the csrf_ token works to thwart csrf attacks. Consider a scenario where an application's /user/email route accepts a POST request to modify the email address of an authenticated user. This route probably anticipates that the user's desired email address will be entered in an email input form. Without CSRF security, a malicious website may produce an HTML form that submits the malicious user's own email address to the application's /user/email route. If the malicious website submits the form automatically as soon as the page loads, the malicious user simply needs to get an application user to visit their website in order for their email address to be altered. Programmers must check each incoming POST, PUT, PATCH, or DELETE request for a secret session value that the malicious application cannot access in order to mitigate this vulnerability.

## Can we create the `<form>` element manually (without using a generator like `{{ form.as_table }}`)?
Of course. We can create `<form>` element manually without using a genereator. To do that, one of the way is create an HTML regio (to serve as a container for your page items), then create items to display in the region, and lastly create processes and branches.

## Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.
After submission, the program will run the `create_task()` to get the title and the description using `request.POST.get()` function. After that, it creates new object in the model that has been created before based on the data that has been submitted. Finally, it reverse to run `show_todolist` function back to the main page, showing all the to do list.

## How to implement?
1. Create new app `todolist` by using this command
```python manage.py startapp todolist```
2. Add todolist URL path by appending `todolist` in the `project_django/settings.py` and add `path('todolist/', include('todolist.urls'))` in `project_django/urls.py`
3. Create model in `todolist/models.py` by using this funtion:
```shell
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```
4. create login, register, and logout function in views.py, then add the routing in urls.py
5. Creating todolist main page by making `show_todolist` function in views.py. Also create ```todolist.html``` to display the main page. Also, add button for add new task and logout.
```shell
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_data = Task.objects.filter(user=request.user)
    context = {"todolist": todolist_data, 
                "username": request.user}
    return render(request, "todolist.html", context)
```
6. Add the url pattern in `todolist/urls.py`
```shell
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path("delete-task/<int:id>", delete_task, name="delete_task"),
    path("update-finished/<int:id>", update_finished, name="update_finished"),
]
```
7. Then, deploy the app in the HEROKU by pull, add, commit, and push to GitHub

# Assignment 05

## What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?

## Describe the HTML5 tags that you know.

## Describe the types of CSS selectors you know.

## Explain how you would implement the checklist above.