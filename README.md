
Mini Django Web Server
======================

This is a very small Python web server that takes inspiration from Django. 

To install this source code, you can either

* Use `git` to checkout this repository into a folder

        cd  (into some folder on your computer where you do programming things)
        git clone https://github.com/csev/mini_django/
  
* Download a zip file from this repository and unzip it into a folder

After you have a copy of the code in a folder on your computer, to run this (assuming you
have Python installed), you navigate into the folder and run the server.

    cd mini_django
    python runserver.py

And navigate to http://localhost:9000

If you want the server to listen on a port other than 9000, add it as an additional parameter on the
`runserver` command.

    python runserver.py 9001

And navigate to http://localhost:9001

Interesting URLs and Views
--------------------------

* http://localhost:9000 is the root path and returns a `text/html` (200) response.
* http://localhost:9000/dj4e returns a `text/plain` (200) response.
* http://localhost:9000/js4e returns a HTTP redirect (302) response. (watch the Network tab of the developer tools)
* http://localhost:9000/broken routes to a view which has a bug that
returns a string instead of an `HttpResponse` object.  The `httpServer()` detects this and returns a HTTP server error
(500) response.
* http://localhost:9000/blah is a path that has no view and so the router
returns a HTTP Page not found (404)

Looking at Code
---------------

There is a PowerPoint presenation describing `mini_django` on the DJ4E web site 
at <a href="https://www.dj4e.com/lectures/mini_django.pptx" target="_blank">https://www.dj4e.com/lectures/mini_django.pptx</a>.

There is a video code walkthrough of this application available at:
at <a href="https://youtu.be/q6LGpiVPwaA" target="_blank">https://youtu.be/q6LGpiVPwaA</a>.

`mini_django.py`

This file is about 200 lines of Python and approximates the entire Django library in a very simple way.  It
handles many aspects of the <a href="https://en.wikipedia.org/wiki/HTTP" target="_blank:">HTTP Network Protocol</a>
like parsing incoming requests, calling your "application router", and sending a correctly formatted the HTTP response
back to the browser to complete the request/response cycle.  This library also defines `HttpRequest` and
`HttpResponse` data classes which are passed into and returned from the application views.

`runserver.py`

This is a very short file.  It loads the `mini_django` library and calls the `httpServer` method
to start listening for connections on the specified port.

`urls.py`

The purpose of this file is to look at the `path` value from the `HttpRequest` object and decide which view
to call.  In "real Django", the paths are stored in an array, but to make easier to understand, this file just
uses a series if `if-then-else` tests to pick the correct view for the path.

`views.py`

This is very similar to the `views.py` in "real Django".  Each view is a function that takes an `HttpRequest`
as its parameter and returns an `HttpResponse` as its return value.  In each view, the code creates
an `HttpResponse` and sets headers in the response and adds the body text to the response and then 
returns it to `mini_django` which then correctly formats the response and sends it back to the browser
to complete the request / response cycle.

AutoGrader Support
------------------

As this code is part of the <a href="https://www.dj4e.com/" target="_blank">Django for Everybody</a>
course, it has the ability to  a small JavaScript library to enable this code to be autograded
as an assignment for the course.  Take a look at the `patchAutograder()` method in `mini_django` for details.

The autograder library is only included in `text/html` responses.

If you want include the autograder library in your application start the web server as follows:

    python runserver.py 9000 autograder

Assuming you have DJ4E running on your computer, you can  do development with a local
copy of the autograder JavaScript endpoint as follows:

    python runserver.py 9000 http://localhost:8888/dj4e/tools/jsauto/autograder.js

