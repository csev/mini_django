import mini_django
import sys
import urls

# For a local Django Application, this is equvalent to
# python manage.py runserver
# For PythonAnywhere, this is like "Reload Application"

# To start the mini_django web server
# python runserver.py
# To start the web server on a different port
# python runserver.py 9001
# To start this with DJ4E autograder support enabled
# python runserver.py 9000 autograder

port = 9000
if len(sys.argv) > 1 :
    port = int(sys.argv[1])

print(f"Access http://localhost:{port}")
mini_django.httpServer(urls.router, port)

