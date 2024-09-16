from django.shortcuts import render

# Create your views here.
def allhero(request):
    return render(request, 'all_avenger.html')