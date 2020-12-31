# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): 
    print(request.user)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "home.html", {'name': 'Nick'})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Ticket Page</h1>")
    about_content = {
        "title": "Ludens - BMTH",
        "practice_text": "'A world covered in cables was never wired to last'",
        "int_title": "Integer: ",
        "practice_int": 324,
        "practice_list": ["for loop", "iterating", "through", "an array", 324]
    }
    return render(request, "about.html", about_content)

