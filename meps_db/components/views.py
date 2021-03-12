from django.http import HttpResponse


def index(request):
    """ Basic HttpResponse """
    return HttpResponse("Go to the admin page")
