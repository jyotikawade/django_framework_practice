from django.http import HttpResponse


def myinfor(request):
    return HttpResponse("<h3>enter music/ in url </h3>")

