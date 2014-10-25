from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!<br>"
                        "<a href=\"about\">About Rango</a>")

def about(request):
    return HttpResponse("Rango says: Here is the about page.<br>"
                        "<a href=\"../rango\">Back to main page</a>")

