from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):
    isActive = True
    if request.method=='POST':
        check=request.POST.get('check')
        print(check)
        if check is None: isActive=False
        else:
            isActive=True   
            
    date = datetime.datetime.now()
    name = "Arslan Sami"
    list_of_program = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prine numbers from 1 to 100',
        'WAP to print pascals traiangle'
    ]
    student={
        "student_name":'Arslan',
        "student_college":"ZYZ",
        "student_city":'Karachi'
    }
    data={
        "date":date,
        'isActive':isActive,
        'name':name,
        'list_of_program':list_of_program,
        'student':student
    }
    return render(request, "home.html", data)


def about(request):
    # return HttpResponse("This is about page")
    return render(request, "about.html")


def services(request):
    # return HttpResponse("This is services page")
    return render(request, "services.html")
    
    
    
    
    
    
    