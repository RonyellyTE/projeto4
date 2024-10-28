from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.
def index_view(request):
    return HttpResponse("Hello There! Welcome to index page")