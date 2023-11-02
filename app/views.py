from django.http import HttpResponse
from django.http.request import HttpRequest


def near_hundred(request, n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def string_splosion(request,str):
    word = ""
    for i in range(len(str)):
        word = word + str[: i + 1]
    return HttpResponse(word)


def cat_dog(request, str):
    if str.count("cat") == str.count("dog"):
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def lone_sum(request, a, b, c):
    if a == b == c:
        return HttpResponse(0)
    if a == b:
        return HttpResponse(c)
    if b == c:
        return HttpResponse(a)
    if a == c:
        return HttpResponse(b)
    else:
        return HttpResponse(a + b + c)

