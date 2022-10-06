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

#### Inline CSS
Inline CSS is used for certain HTML tags. The `<style>` attribute is used to style certain HTML tags. This method is not recommended, because each HTML tag must be styled in its own way.
```
<!DOCTYPE html>
<html>
<body style="background-color:black;">
 
<h1 style="color:white;padding:30px;">Hostinger Tutorials</h1>
<p style="color:white;">Something usefull here.</p>
 
</body>
</html>
```
**Advantages**: Useful for trial and error to see the changes, quick changes, small HTTP request
**Disadvantages**: Need to be applied in every element

#### Internal CSS
The internal CSS code is placed inside the `<head>` section of the page. Class and ID can be used to refer to CSS code, but will only be active on that page. CSS styles installed with this method will be downloaded every time the page is called, so this will increase the access speed. However, there are cases where using internal stylesheets is useful. One example is to send a page template to someone – since everything can be seen on one page, it's easier to preview. The internal CSS is placed inside the `<style></style>` tag.
```
<head>
  <style type="text/css">
    p {color:white; font-size: 10px;}
    .center {display: block; margin: 0 auto;}
    #button-go, #button-back {border: solid 1px black;}
  </style>
</head>
```
**Advantages**: Changes only occur on 1 page, class and ID can be used by internal stylesheets. There is no need to upload multiple files because HTML and CSS can be used in the same file.
**Disadvantages**: Increase website access time, changes only occur on one page,  not efficient when we want to use the same CSS across multiple files.

#### External CSS
One of the most convenient ways to add CSS to your website is by linking it to an external `.css` file. That way, any changes you make to the CSS file will appear on your website as a whole. External CSS files are usually placed after the `<head>` section of the page:
```
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
```
While, the content example for the style.css as shown below:
```
.login-box a:hover {
  background: #03e9f4;
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px #03e9f4,
              0 0 25px #03e9f4,
              0 0 50px #03e9f4,
              0 0 100px #03e9f4;
}

.login-box a span {
  position: absolute;
  display: block;
```
**Advantages**: The HTML file size is smaller and the structure is neater, faster loading speed, the same CSS file can be used on multiple pages.
**Disadvantages**: The page does not appear completely until the CSS file has been called.

## Describe the HTML5 tags that you know.
```
Tag	Description
<!--...-->	    Specifies a comment
<!DOCTYPE>	    Specifies the document type
<a>	            Specifies an anchor
<abbr>	        Specifies an abbreviation
<acronym>	    Deprecated:Specifies an acronym
<address>	    Specifies an address element
<applet>	    Deprecated: Specifies an applet
<area>	        Specifies an area inside an image map
<article>	    New Tag: Specifies an independent piece of content of a document, such as a blog entry or newspaper article
<aside>	        New Tag:Specifies a piece of content that is only slightly related to the rest of the page.
<audio>	        New Tag:Specifies an audio file.
<base>	        Specifies a base URL for all the links in a page
<basefont>	    Deprecated: Specifies a base font
<bdo>	        Specifies the direction of text display
<bgsound>	    Specifies the background music
<blink>	Specifies a text which blinks
<blockquote>	Specifies a long quotation
<body>	Specifies the body element
<br>	Inserts a single line break
<button>	Specifies a push button
<canvas>	New Tag:This is used for rendering dynamic bitmap graphics on the fly, such as graphs or games.
<caption>	Specifies a table caption
<center>	Deprecated: Specifies centered text
<col>	Specifies attributes for table columns 
<colgroup>	Specifies groups of table columns
<command>	New Tag:Specifies a command the user can invoke.
<comment>	Puts a comment in the document
<datalist>	New Tag:Together with the a new list attribute for input can be used to make comboboxes
<dd>	Specifies a definition description
<del>	Specifies deleted text
<details>	New Tag:Specifies additional information or controls which the user can obtain on demand.
<dir>	Deprecated: Specifies a directory list
<div>	Specifies a section in a document
<b>	Specifies bold text
<font>	Deprecated: Specifies text font, size, and color
<form>	Specifies a form 
<frame>	Deprecated:Specifies a sub window (a frame)
<head>	Specifies information about the document
<header>	New Tag:Specifies a group of introductory or navigational aids.
<h1> to <h6>	Specifies header 1 to header 6
<hr>	Specifies a horizontal rule
<html>	Specifies an html document
<img>	Specifies an image
<input>	Specifies an input field
<label>	Specifies a label for a form control
<li>	Specifies a list item
<link>	Specifies a resource reference
<mark>	New Tag:Specifies a run of text in one document marked or highlighted for reference purposes, due to its relevance in another context.
<nav>	New Tag:Specifies a section of the document intended for navigation.
<p>	Specifies a paragraph
<code>	Specifies computer code text
<script>	Specifies a script
<section>	New Tag:Represents a generic document or application section.
<span>	Specifies a section in a document
<style>	Specifies a style definition
<table>	Specifies a table
<tbody>	Specifies a table body
<td>	Specifies a table cell
<th>	Specifies a table header
<thead>	Specifies a table header
<title>	Specifies the document title
<tr>	Specifies a table row
<u>	Deprecated: Specifies underlined text
<ul>	Specifies an unordered list
```

## Describe the types of CSS selectors you know.
1. Universal Selector
Selects all elements. Optionally, it may be restricted to a specific namespace or to all namespaces.
Syntax: `* ns|* *|*`
Example: `*` will match all the elements of the document.

2. Type Selector
Selects all elements that have the given node name.
Syntax: `elementname`
Example: input will match any `<input>` element.

3. Class Selector
Selects all elements that have the given class attribute.
Syntax: `.classname`
Example: `.index` will match any element that has `class="index"`.

4. ID Selector
Selects an element based on the value of its id attribute. There should be only one element with a given ID in a document.
Syntax: `#idname`
Example: `#toc` will match the element that has `id="toc"`.

5. Attribute Selector
Selects all elements that have the given attribute.
Syntax: `[attr] [attr=value] [attr~=value] [attr|=value] [attr^=value] [attr$=value] [attr*=value]`

Example: `[autoplay]` will match all elements that have the `autoplay` attribute set (to any value).

## Explain how you would implement the checklist above.
The UI Kit that I used for this app is Bootstrap. Firstly, I add the bootstrap reference in the `base.html` so that when template extend the base, it applies the bootstrap. Then, I start decorating the login page, register page, todolist main page, and the create new task page. In the register and login page, the designs are pretty simple, just add the div for the forms and add rounded background so it's looks nice and tidy. Then, for the main page, I use cards for listing all the todolist, and also it can change the color of the card header depends on the task status. I also add the navbar for the main page and the create new task. Instead of adding button for redirecting to the create new task, I add one page(menu) in the navbar to create new task.