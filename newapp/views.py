from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello from changing_view_response Branch!")

