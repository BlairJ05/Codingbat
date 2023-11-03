from django.http import HttpResponse
from django.http.request import HttpRequest

#If the number is 10 numbers from 100 or 200 it returns true
def near_hundred(request:HttpRequest, n:int):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

# I have an i variable for every letter in the string then I return the word 
def string_splosion(request:HttpRequest,str:str):
    word = ""
    for i in range(len(str)):
        word = word + str[: i + 1]
    return HttpResponse(word)

# This if statment looks through the string and looks for cat and dog. if cat and dog exist in the same string it will return true
def cat_dog(request:HttpRequest, str:str):
    if str.count("cat") == str.count("dog"):
        return HttpResponse(True)
    else:
        return HttpResponse(False)

# This will make sure that none of  variables are the same number then it adds the numbers that are not the same
def lone_sum(request:HttpRequest, a:int, b:int, c:int):
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

