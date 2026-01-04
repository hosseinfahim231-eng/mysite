from django.http import HttpResponse


def http_test(request):
    return HttpResponse("Hello World")
# Create your views here.
