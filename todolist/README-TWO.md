# LINKS
[HOME](https://pbp-assg-2.herokuapp.com) -
[TODOLIST](https://pbp-assg-2.herokuapp.com/todolist/)

## Describe the difference between asynchronous programming with synchronous programming.
In synchronous operations tasks are performed one at a time and only when one is completed, the following is unblocked. In other words, we need to wait for a task to finish to move to the next one. In asynchronous operations, on the other hand, we can move to another task before the previous one finishes. This way, with asynchronous programming we’re able to deal with multiple requests simultaneously, thus completing more tasks in a much shorter period of time.
[source](https://www.outsystems.com/blog/posts/asynchronous-vs-synchronous-programming/)

## When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.
The main focus of event-driven programming is events. Program flow ultimately depends on external events. The model containing the concept of event-driven programming is known as an asynchronous model. Up to this point, we have only dealt with sequential or parallel execution models. Event-driven programming relies on an event loop that is constantly watching for brand-new occurrences that have just occurred. Events are necessary for event-driven programming to function. Events select what to do and in what order to perform it once they have looped.
[]()

## Describe the implementation of asynchronous programming in AJAX.
AJAX allows web pages to be updated asynchronously by exchanging small amounts of data with the server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page. use jQuery’s ajax() function to call backend function asynchronously or in other words HTTP Requests. The jQuery $.ajax() function is used to perform an asynchronous HTTP request. It was added to the library a long time ago, existing since version 1.0. The $.ajax() function is what every function discussed in the previously mentioned article calls behind the scene using a preset configuration. 
[source 1](https://www.w3schools.com/php/php_ajax_intro.asp#:~:text=AJAX%20allows%20web%20pages%20to,if%20the%20content%20should%20change.)
[source 2](https://www.geeksforgeeks.org/how-to-use-jquerys-ajax-function-for-asynchronous-http-requests/)

## How to implement
1. Create a view that returns the whole data task in the form of JSON.
2. Create a path containing /todolist/json that redirects to the new view that you've just made
3. Create an Add Task button that opens to a modal with a form to add new tasks.
4. Implement GET and POST to fetch and display the data using AJAX