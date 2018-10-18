from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey World. You're at the polls index.'")
