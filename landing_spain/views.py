from django.shortcuts import render
from django.http import HttpResponse

from .forms import SearchForm

def home(request):
    if request.method == "POST":
        
        search_form = SearchForm({
            "city": request.POST.get("city", None),
            "date_arrival" : request.POST.get("date_arrival", None),
            "date_departure" : request.POST.get("date_departure", None),
            "guest" : request.POST.get("guest", None)
        })
        
        if not search_form.is_valid():
            # return HttpResponse(search_form.errors)
            print(search_form.errors)

        print("clean data: ", search_form.cleaned_data)
    
    return render(
        request=request, 
        template_name="landing_spain/home.html", 
        context={
        "cities": ["barcelona", "madrid", "valencia"],
        "guests": [1, 2, 3, 4]
        }
    )