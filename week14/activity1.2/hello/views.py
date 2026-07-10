from django.http import HttpResponse


def home(request):
    """Display the Week 14 greeting."""
    return HttpResponse('<h1>Hello Django</h1>')
