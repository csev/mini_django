
from mini_django import HttpRequest, HttpResponse

# This is similar to Django's views.py

def root(req: HttpRequest) -> HttpResponse:
    res = HttpResponse()
    res.headers['Content-Type'] = 'text/html; charset=utf-8'
    res.write("<!DOCTYPE html>")
    res.write("<html><head></head><body>")
    res.write("<p>mini_django seems to be working!</p>")
    res.write("<p>This is the page at the root path, try another path</p>")
    res.write("<p>Try /dj4e /js4e or generate errors with /missing or /broken</p>")
    res.write("</body></html>")
    return res

def dj4e(req: HttpRequest) -> HttpResponse:
    res = HttpResponse()
    res.headers['Content-Type'] = 'text/plain; charset=utf-8'
    res.write("Django is fun")
    return res

def js4e(req: HttpRequest) -> HttpResponse:
    res = HttpResponse()
    res.code = "302"    # Lets do a temporary redirect...
    res.headers['Location'] = '/dj4e'
    res.headers['Content-Type'] = 'text/plain; charset=utf-8'
    res.write("You will only see this in the debugger!")
    return res

def broken(req: HttpRequest):
    return "I am a broken view, returning a string by mistake"






