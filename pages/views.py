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
        "title": "About",
        "practice_text": "This query ticket application was created by Christine.",
        
    }
    return render(request, "about.html", about_content)

